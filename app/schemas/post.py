from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostType(str, Enum):
    video = "video"
    image = "image"
    song = "song"

class Post(BaseModel):
    post_type: Optional[PostType] = "image"
    post_content: str  # S3 BUCKET LINK? NOT SURE YET

class MultiPost(BaseModel):
    posted_at: datetime.datetime
    posts: list[Post]