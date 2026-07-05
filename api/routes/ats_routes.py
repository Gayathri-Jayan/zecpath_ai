from fastapi import APIRouter

router = APIRouter()

@router.post("/ats/score")
def score_candidate():

    return {

        "candidate_id": "C123",

        "final_score": 86.5
    }