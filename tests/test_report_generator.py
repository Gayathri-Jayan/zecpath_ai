from screening_ai.report_generator import (
    generate_screening_report,
    export_report
)

candidate = {
    "candidate_id": "C123",
    "job_id": "J101"
}

answers = [
    {
        "question_id": "Q3",
        "original_text": "I have 3 years experience in Python and Django.",
        "skills": ["python", "django"],
        "salary": "8 LPA",
        "availability": "Immediate",
        "overall": 92,
        "is_vague": False
    }
]

report = generate_screening_report(
    candidate,
    answers
)

print(report)

print()

export_report(report)