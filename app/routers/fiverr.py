from fastapi import APIRouter

router = APIRouter(prefix="/fiverr", tags=["Fiverr"])

@router.get("/jobs")
def fetch_fiverr_jobs():
    return {"platform": "fiverr", "jobs": []}