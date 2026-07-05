

from ats_engine.eligibility_engine import (
    evaluate_candidate
)


def test_eligibility():

    candidate = {

        "candidate_id": "C123",

        "final_score": 80,

        "skills": [

            "Python",

            "Django"
        ],

        "total_experience": 3,

        "location": "Bangalore",

        "available": True
    }

    rules = {

        "min_ats_score": 75,

        "mandatory_skills": [

            "Python"
        ],

        "min_experience": 2,

        "max_experience": 5,

        "allowed_locations": [

            "Bangalore"
        ],

        "availability_required": True
    }

    result = evaluate_candidate(

        candidate,

        rules)

    print(result)

    assert result[

        "eligibility_status"

    ] == "Eligible"


test_eligibility()