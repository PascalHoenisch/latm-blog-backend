from http.client import HTTPException

from fastapi import FastAPI
from helper.db import authors, blogs, get_authors
from model.Author import Author
from model.BlogPost import BlogPost

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    return {"healthcheck": "success"}


@app.get("/favicon.ico")
def favicon():
    return


@app.get("/authors")
async def get_all_authors() -> list[Author]:
    try:
        # get all authors from the collection
        author_models = await get_authors(limit=10)
        return author_models
    except Exception as e:
        return str(e)


@app.get("/posts")
async def get_all_posts() -> list[BlogPost]:
    try:
        # get all authors from the collection
        authors_models = await get_authors(limit=10)

        # Map authors name with their object
        authors_map = {author.name: author for author in authors_models}

        # get all posts from the collection
        post_list = blogs.find()
        post_models = []

        async for doc in post_list:
            # joining the author
            doc['author'] = authors_map[doc['author']]
            # get posts
            post = BlogPost(**doc)
            post_models.append(post)

        # check if list is empty
        if not post_list:
            raise HTTPException(status_code=404, detail="List is empty")

        return post_models
    except Exception as e:
        return str(e)


