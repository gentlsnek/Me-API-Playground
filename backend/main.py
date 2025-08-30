from fastapi import FastAPI
from routes import projects, skills, profile

app = FastAPI()

# Register routers
app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(profile.router)

@app.get("/")
def root():
    return {"message": "FastAPI backend running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
