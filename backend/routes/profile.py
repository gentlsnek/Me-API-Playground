from fastapi import APIRouter
from models import get_profile, update_profile

router = APIRouter()

@router.get("/profile")
def read_profile():
    return get_profile()

@router.get("/profile/update")
def profile_update(category: str, subject: str):
    return update_profile(category, subject)