import pprint
from helper.env import config
from helper.image_tools import generate_signed_url
from helper.md_converter import convert_to_html
from model.Author import Author, ProcessedAuthor, PreviewAuthor
from model.Translation import LanguageOption
from model.Image import ProcessedImage, Image
from model.BlogPost import SizeOption, ProcessedPost
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(config["MONGO_URL"])
db = client[config["BLOG_DB"]]
authors = db["authors"]
posts = db["posts"]


def get_authors(limit: int) -> list[Author]:
    authors_list = authors.find().limit(limit)
    authors_models = []

    for doc in authors_list:
        author = Author(**doc)
        authors_models.append(author)

    return authors_models


def get_processed_authors(lang: LanguageOption) -> list[ProcessedAuthor]:
    author_models = get_authors(10)
    # map all authors as a processedAuthor and the slogan and image depending on the lang
    processed_authors = [
        ProcessedAuthor(
            name=author.name,
            slogan=author.slogan[lang.value],
            image=ProcessedImage(
                path=author.previewImage.icon_size if author.previewImage.icon_size is not None else '',
                description=author.previewImage.description[lang.value]
            )
        )
        for author in author_models
    ]

    return processed_authors


def get_posts(lang: LanguageOption, size: SizeOption, limit: int) -> list[ProcessedPost]:
    posts_list = posts.find().limit(limit)
    processed_authors_by_lang = get_processed_authors(lang=lang)
    posts_models = []

    for doc in posts_list:
        # Find the corresponding author by name from the processed authors list
        author_name = doc['author']
        author = next((a for a in processed_authors_by_lang if a.name == author_name), None)

    posts_list = posts.find().limit(limit)
    processed_authors_by_lang = get_processed_authors(lang=lang)
    posts_models = []

    for doc in posts_list:
        author = find_author_by_name(processed_authors_by_lang, doc['author'])
        content = get_content(doc, lang, size)
        if content_needs_update(doc, lang, size):
            update_content_in_db(doc['_id'], content, size, lang)

        if needs_image_update(doc):
            update_title_image_in_db(doc['_id'], doc['title_image'])

        post = create_processed_post(doc, lang, size, author, content)
        posts_models.append(post)

    return posts_models


def title_image_needs_update(doc):
    # Implement the logic to check if the title image needs an update
    
    title_image = doc.get('title_image', {})

    # Check if required sizes are present and valid
    required_sizes = ['icon_size', 'sm_size', 'md_size', 'lg_size']
    for size in required_sizes:
        if size not in title_image or not title_image[size]:
            return True

    # Additional logic to determine if the title image needs an update can go here
    # For example, if the images are out of date or not in sync, add the conditions here
    return False


def update_title_image_in_db(id: str, image: dict):
    # Checking the type of image and adapting accordingly
    if isinstance(image, dict):
        signed_urls = {
            'icon_size': generate_signed_url(image.get('icon_size', ''), SizeOption.icon_size),
            'sm_size': generate_signed_url(image.get('sm_size', ''), SizeOption.sm_html),
            'md_size': generate_signed_url(image.get('md_size', ''), SizeOption.md_html),
            'lg_size': generate_signed_url(image.get('lg_size', ''), SizeOption.lg_html),
        }
    else:
        signed_urls = {
            'icon_size': generate_signed_url(image.icon_size, SizeOption.icon_size),
            'sm_size': generate_signed_url(image.sm_size, SizeOption.sm_html),
            'md_size': generate_signed_url(image.md_size, SizeOption.md_html),
            'lg_size': generate_signed_url(image.lg_size, SizeOption.lg_html),
        }

    pprint.pprint(signed_urls)

    posts.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            'title_image.icon_size': signed_urls['icon_size'],
            'title_image.sm_size': signed_urls['sm_size'],
            'title_image.md_size': signed_urls['md_size'],
            'title_image.lg_size': signed_urls['lg_size'],
        }}
    )

def update_post_if_needed(doc, content, lang, size):
    if content_needs_update(doc, lang, size) or title_image_needs_update(doc):
        update_content_in_db(doc['_id'], content, size, lang)
        # Assume update_title_image_in_db method handles updating the title image
        update_title_image_in_db(doc['_id'], doc['title_image'])
        
        
def find_author_by_name(authors, author_name):
    return next((a for a in authors if a.name == author_name), None)


def get_content(doc, lang, size):
    html_content = doc['content'][size.name][lang.value]
    markdown_content = doc['content']['md'][lang.value]
    return html_content if html_content is not None else convert_to_html(markdown_content,
                                                                         size=size) if markdown_content else ''


def content_needs_update(doc, lang, size):
    return needs_content_update(doc, lang, size) or needs_image_update(doc)


def needs_content_update(doc, lang, size):
    content = doc['content']
    size_content = content[size.name][lang.value]
    md_content = content['md'][lang.value]
    return size_content is None and md_content is not None


def needs_image_update(doc):
    title_image = doc['title_image']
    return any(title_image.get(size_name) is None for size_name in ['icon_size', 'sm_size', 'md_size', 'lg_size'])


def update_content_in_db(post_id, content, size, lang):
    posts.update_one(
        {'_id': post_id},
        {'$set': {f'content.{size.name}.{lang.value}': content}}
    )


def create_processed_post(doc, lang, size, author, content):
    return ProcessedPost(
        id=str(doc['_id']),
        title=doc['title'][lang.value],
        slug=doc['slug'][lang.value],
        description=doc['description'][lang.value],
        content=content,
        tag=doc['tag'],
        date=doc['date'],
        author=author,
        title_image=ProcessedImage(
            path=doc['title_image']['sm_size'] if doc['title_image']['sm_size'] is not None else '',
            description=doc['title_image']['description'][lang.value]
        )
    )


def find_post(lang: LanguageOption, size: SizeOption, post_id: str, slug: str) -> ProcessedPost | None:
    authors_models = get_processed_authors(lang=lang)
    authors_map = {author.name: author for author in authors_models}

    # find the post by its id
    post = posts.find_one({"_id": ObjectId(post_id)})

    if not post:
        return None

    if post.get('slug', {}).get(lang.value) != slug:
        return None

    return ProcessedPost(
        id=str(post.get('_id')),
        title=post.get('title', {}).get(lang.value, '') or '',
        slug=post.get('slug', {}).get(lang.value, ''),
        description=post.get('description', {}).get(lang.value, '') or '',
        content=post.get('content', {}).get(str(size.name), {}).get(lang.value, '') or '',
        tag=post.get('tag', []) or [],
        date=post.get('date'),
        title_image=ProcessedImage(
            path=post.get('title_image', {}).get(size.value, ''),
            description=post.get('title_image', {}).get('description', {}).get(lang.value, '') or ''
        ),
        author=authors_map[post.get('author', {})]
    )
