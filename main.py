from fastapi import FastAPI
from fastapi.param_functions import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Stefan"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_post(payload: dict = Body(...)):
    return {"new_post": f"title {payload['title']}, content {payload['content']}"}