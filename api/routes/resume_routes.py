from fastapi import APIRouter

router = APIRouter()

@router.post("/resume/upload")
def upload_resume():

    return {

        "status": "success",

        "message":
        "Resume uploaded successfully",

        "resume_id": "R456"
    }