from pydantic import BaseModel

class Candidate(BaseModel):

    candidate_id: str

    resume_id: str

    skills: list

    experience: list

    education: list