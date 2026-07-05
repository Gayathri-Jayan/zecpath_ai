from ats_engine.semantic_matcher import (

    match_resume_to_jd,

    classify_match
)


resume = {

    "skills": [
        "Python",
        "Django"
    ],

    "experience": [

        {
            "role": "Backend Developer"
        }
    ],

    "projects": [

        {
            "description":
            "API development using Django"
        }
    ]
}


jd = {

    "job_title": "Backend Developer",

    "required_skills": [
        "Python",
        "Django"
    ],

    "job_description_text":
    "Build APIs and backend services"
}


result = match_resume_to_jd(
    resume,
    jd
)

match_type = classify_match(
    result["final_similarity_score"]
)

print(result)

print(
    "Match Type:",
    match_type
)