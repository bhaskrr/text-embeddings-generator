
from service.api.routes import tfidf_route
from service.api.routes.word2vec import word2vec_route

from fastapi.routing import APIRouter

embedding_router = APIRouter()

embedding_router.include_router(tfidf_route, prefix='/tfidf')
embedding_router.include_router(word2vec_route, prefix= '/word2vec')