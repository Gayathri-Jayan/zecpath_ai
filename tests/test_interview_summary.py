from interview_ai.interview_summary_generator import generate_interview_summary

candidate = {

    "candidate_id": "C101",

    "communication_score": 86,

    "confidence_score": 92,

    "aptitude_score": 80,

    "teamwork": True,

    "adaptability": True,

    "stress_score": 0.8,

    "contradiction": False,

    "is_vague": False
}

result = generate_interview_summary(candidate)

print(result)