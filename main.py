from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
def root():
    return {"healthcheck": "success"}
