from typing import Union

from fastapi import FastAPI

from .api.main import embedding_router

app = FastAPI()


@app.get("/")
def home():
    return {"This is the root route for the embeddings generator app"}


app.include_router(embedding_router, prefix='/embeddings')