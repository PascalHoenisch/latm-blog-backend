from http.client import HTTPException
from pprint import pprint

from fastapi import FastAPI, Query
from helper.db import posts, get_authors, find_post, get_preview_authors
from model.Author import Author, ProcessedAuthor
from model.Translation import LanguageOption
from typing import Annotated
from model.BlogPost import ProcessedPost, SizeOption, BlogPost

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    return {"healthcheck": "success"}


@app.get("/favicon.ico")
def favicon():
    return


@app.get("/all/authors")
async def get_all_authors() -> list[Author]:
    try:
        # get all authors from the collection
        author_models = get_authors(limit=10)
        return author_models
    except Exception as e:
        return str(e)


@app.get("/all/posts")
async def get_all_posts(
        lang: Annotated[LanguageOption, Query(
            description="The language the blogs will have"
        )],
        size: Annotated[SizeOption, Query(
            description="The size the images should have."
        )],
) -> list[ProcessedPost] | list[ProcessedAuthor]:
    try:
        # get all authors from the collection
        authors_models = get_preview_authors(lang=lang)

        return authors_models
        # Map authors name with their object
        authors_map = {author.name: author for author in authors_models}

        # get all posts from the collection
        post_list = posts.find()
        post_models = []

        for doc in post_list:
            # joining the author
            doc['author'] = authors_map[doc['author']]
            # get posts
            post = ProcessedPost(**doc)
            post_models.append(post)

        # check if list is empty
        if not post_list:
            raise HTTPException(status_code=404, detail="List is empty")

        return post_models
    except Exception as e:
        return str(e)


@app.get("/post")
async def get_specific_post(
        lang: Annotated[LanguageOption, Query(
            description="The language the slug will be queried after. Also determens in which language the post will "
                        "be returned."
        )],
        size: Annotated[SizeOption, Query(
            description="The size the images should have."
        )],
        post_id: Annotated[str, Query(
            min_length=1,
            max_length=200,
            title="Query String",
            description="Post id."
        )]) -> ProcessedPost | None:
    try:
        post = find_post(lang, size, post_id)

        return post
    except Exception as e:
        return str(e)
