from fastapi import FastAPI
from routes import projects, skills, profile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Register routers
app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(profile.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://127.0.0.1:3000"] for security
    allow_credentials=True,
    allow_methods=["*"],   # ["GET", "POST"] if you want to restrict
    allow_headers=["*"],   # Or specific headers
)


@app.get("/")
def root():
    return {"message": "FastAPI backend running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
