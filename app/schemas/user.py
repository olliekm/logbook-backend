from pydantic import BaseModel, Field

class User(BaseModel):
    uuid: int
    username: str
    display_name: str
    password: str
    private: bool
    following: list[int]
    followers: list[int]