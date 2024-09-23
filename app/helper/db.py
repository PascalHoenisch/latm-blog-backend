import pprint
from typing import List

from helper.env import config
from model.Author import Author, ProcessedAuthor, PreviewAuthor
from model.Translation import LanguageOption
from model.Image import ProcessedImage
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


def get_preview_authors(lang: LanguageOption) -> list[ProcessedAuthor]:
    author_models = get_authors(10)
    # map all authors as a processedAuthor and the slogan and image depending on the lang
    preview_authors = [
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

    return preview_authors


def find_post(lang: LanguageOption, size: SizeOption, post_id: str) -> ProcessedPost | None:
    authors_models = get_authors(10)
    authors_map = {author.name: author for author in authors_models}

    # find the post by its id
    post = posts.find_one({"_id": ObjectId(post_id)})

    pprint.pprint(post)
    return None
    post_model = None

    for doc in post:
        pprint.pprint(doc['title'])
        return None
        # mapping the language and size values to a simplified and shortened version of a blog post

        post_model = ProcessedPost(
            title=doc['title'][lang],
            slug=doc['slug'][lang],
            description=doc['description'][lang],
            content=doc['content'][size][lang],
            tag=doc['tag'],
            date=doc['date'],
            title_image=ProcessedImage(
                path=doc['title_image'][size],
                description=doc['title_image']['description'][lang]
            ),
            author=ProcessedAuthor(
                name=doc['author']['name'],
                slogan=doc['author']['slogan'][lang],
                image=ProcessedImage(
                    path=doc['title_image']['icon_size'],
                    description=doc['title_image']['description'][lang]
                )
            )
        )

    return post_model
