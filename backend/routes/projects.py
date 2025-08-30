from fastapi import APIRouter
from models import create_project, get_projects, update_project, delete_project, get_project_by_skill

router = APIRouter()

@router.get("/projects/get")
def read_projects():
    return get_projects()

@router.get("/projects/byskills/get/{skill}")
def read_projects_byskill(skill: str):
    return get_project_by_skill(skill);
