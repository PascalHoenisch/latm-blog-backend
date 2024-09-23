from http.client import HTTPException
from pprint import pprint

from fastapi import FastAPI, Query
from helper.db import posts, get_authors, find_post, get_processed_authors, get_posts
from model.Author import Author, ProcessedAuthor
from model.Image import ProcessedImage, Image
from model.Translation import LanguageOption
from typing import Annotated
from model.BlogPost import ProcessedPost, SizeOption, BlogPost, ProcessedPreviewPost

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
        raise HTTPException()


@app.get("/all/posts")
async def get_all_posts(
        lang: Annotated[LanguageOption, Query(
            description="The language the blogs will have"
        )],
        size: Annotated[SizeOption, Query(
            description="The size the images should have."
        )],
) -> list[ProcessedPost]:
    try:
        # get all posts from the collection
        post_list = get_posts(lang=lang, size=size, limit=1000)

        return post_list
    except HTTPException as http_exc:
        raise http_exc


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
        raise HTTPException()
