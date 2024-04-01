from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    return {"healthcheck": "success"}


@app.get("/all")
def get_all():
    return 1
