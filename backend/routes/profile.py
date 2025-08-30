from fastapi import APIRouter
from models import get_profile

router = APIRouter()

@router.get("/profile")
def read_profile():
    return get_profile()
