from pydantic import BaseModel

class Post(BaseModel):
    text: str
    #description: Union[str, None] = None

class User(BaseModel):
    email: str
    password: str