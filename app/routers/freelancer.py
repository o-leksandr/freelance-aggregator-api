from fastapi import APIRouter

router = APIRouter(prefix="/freelancer", tags=["Freelancer"])

@router.get("/jobs")
def fetch_freelancer_jobs():
    return {"platform": "freelancer", "jobs": []}