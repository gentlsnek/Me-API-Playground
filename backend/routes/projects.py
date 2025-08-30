from fastapi import APIRouter
from models import create_project, get_projects, update_project, delete_project

router = APIRouter()

@router.post("/project")
def add_project(data: dict):
    return create_project(data)

@router.get("/projects")
def read_projects():
    return get_projects()

@router.put("/project/{project_id}")
def edit_project(project_id: int, data: dict):
    return update_project(project_id, data)

@router.delete("/project/{project_id}")
def remove_project(project_id: int):
    return delete_project(project_id)
