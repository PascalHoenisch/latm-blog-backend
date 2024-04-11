from motor.motor_asyncio import AsyncIOMotorClient
from helper.env import config


client = AsyncIOMotorClient(config["MONGO_URL"])
db = client[config["BLOG_DB"]]
authors = db["authors"]
blogs = db["blogs"]
