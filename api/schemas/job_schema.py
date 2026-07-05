from pydantic import BaseModel

class Job(BaseModel):

    job_id: str

    job_title: str

    required_skills: list

    experience_required: int