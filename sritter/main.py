from typing import Union

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Post(BaseModel):
    text: str
    #description: Union[str, None] = None

class User(BaseModel):
    email: str
    password: str


@app.get("/")
def read_root():
    return  {"Hello": "sdsad"}

@app.get("/api/v1/posts/")
async def getAllPosts(limit: Union[int, None] = None, offset: Union[int, None] = None):
    posts = [
            {"text": "текст поста 0"},
            {"text": "текст поста 1"},
            {"text": "текст поста 2"},
            {"text": "текст поста 3"},
        ]
    try:
        return posts[offset:offset+limit]
    except:
        return 'что-то пошло не так'

@app.post("/create_posts/")
async def create_post(request: Request, item: Post):
    if(request.headers["authorization"] != "Bearer asdasda34r235sdaf4352b34t3v2466b236jh%^&ytg568td"):
        raise HTTPException(status_code=403, detail="wrong token")
    return item

@app.post("/api/v1/users/register/")
async def create_user(user: User):
    print(user)
    return user

@app.post("/api/v1/users/authenticate")
async def auth():
    return "asdasda34r235sdaf4352b34t3v2466b236jh%^&ytg568td"