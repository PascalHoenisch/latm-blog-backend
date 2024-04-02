from fastapi import FastAPI
from helper.db import authors, blogs
from model.Author import Author

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    return {"healthcheck": "success"}


@app.get("/authors/all")
async def get_all():
    try:
        # get all authors from the collection
        authors_list = authors.find().limit(10)
        authors_models = []

        async for doc in authors_list:
            author = Author(**doc)
            authors_models.append(author)
        return authors_models
    except Exception as e:
        return str(e)
