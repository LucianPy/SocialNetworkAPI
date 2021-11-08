from . import models

from fastapi import FastAPI
from psycopg2.extras import RealDictCursor

from .database import engine
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
