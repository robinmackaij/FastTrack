from fastapi import FastAPI

from demo_api.routers.author import author_router
from demo_api.routers.poem import poem_router


def create_app():
    app = FastAPI()
    app.include_router(author_router)
    app.include_router(poem_router)

    return app


api = create_app()
