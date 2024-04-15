from motor.motor_asyncio import AsyncIOMotorClient
from helper.env import config
from model.Author import Author
from model.Translation import LanguageOption
from model.BlogPost import BlogPost

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


async def find_post(lang: LanguageOption, slug: str) -> BlogPost | None:
    authors_models = get_authors(10)
    authors_map = {author.name: author for author in authors_models}

    post = blogs.find({'slug': {lang.value: slug}}).limit(1)
    post_model = None

    async for doc in post:
        # joining the author
        doc['author'] = authors_map[doc['author']]
        # get posts
        post_model = BlogPost(**doc)
        # joining the author
    return post_model
