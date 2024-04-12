from motor.motor_asyncio import AsyncIOMotorClient
from helper.env import config
from model.Author import Author

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
