from fastapi import FastAPI
from app.routers import upwork, fiverr, freelancer

app = FastAPI(title="Freelance Aggregator API")

# Include routers (even if empty for now)
app.include_router(upwork.router)
app.include_router(fiverr.router)
app.include_router(freelancer.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Freelance Aggregator API 🚀"}

@app.get("/jobs")
def get_jobs():
    return {"jobs": []}  # Placeholder
    