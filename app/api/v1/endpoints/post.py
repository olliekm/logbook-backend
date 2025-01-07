from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.post import PostCreate, PostResponse
from app.services.post_service import create_post, get_posts_by_user

router = APIRouter()

@router.post("/", response_model=PostResponse)
def create_new_post(post: PostCreate, db: Session = Depends(get_db)):
    """
    Create a new post.
    """
    return create_post(db, post)

@router.get("/user/{user_id}", response_model=list[PostResponse])
def get_user_posts(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all posts by a specific user.
    """
    posts = get_posts_by_user(db, user_id)
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found for this user.")
    return posts

@router.post("/upload/")
def upload_image(file: UploadFile = File(...)):
    """
    Upload an image file for a post.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type.")
    # Logic for saving the file would go here
    return {"filename": file.filename}
