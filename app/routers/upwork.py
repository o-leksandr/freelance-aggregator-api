from fastapi import APIRouter

router = APIRouter(prefix="/upwork", tags=["Upwork"])

@router.get("/jobs")
def fetch_upwork_jobs():
    return {"platform": "upwork", "jobs": []}