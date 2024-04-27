from motor.motor_asyncio import AsyncIOMotorClient
from helper.env import config
from model.Author import Author, ProcessedAuthor
from model.Translation import LanguageOption
from model.Image import ProcessedImage
from model.ProcessedPost import SizeOption, ProcessedPost

client = AsyncIOMotorClient(config["MONGO_URL"])
db = client[config["BLOG_DB"]]
authors = db["authors"]
blogs = db["blogs"]


async def get_authors(limit: int) -> list[Author]:
    authors_list = authors.find().limit(limit)
    authors_models = []

    async for doc in authors_list:
        author = Author(**doc)
        authors_models.append(author)

    return authors_models


async def find_post(lang: LanguageOption, size: SizeOption, slug: str) -> ProcessedPost | None:
    authors_models = await get_authors(10)
    authors_map = {author.name: author for author in authors_models}

    post = blogs.find({'slug': {lang.value: slug}}).limit(1)

    post_model = None

    async for doc in post:
        print(doc['slug'])

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
