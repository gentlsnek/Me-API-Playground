from fastapi import APIRouter
from models import get_top_skills

router = APIRouter()

@router.get("/skills/top")
def read_top_skills():
    return get_top_skills()
