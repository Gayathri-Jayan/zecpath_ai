from screening_ai.answer_understanding_engine import understand_answer
from screening_ai.screening_scorer import score_answer
from screening_ai.confidence_sentiment import analyze_behavior
from screening_ai.report_generator import generate_screening_report

candidate = {
    "candidate_id": "C123",
    "job_id": "J101"
}

answer = "I have 3 years experience in Python and Django."

# Step 1 - Understand Answer
structured = understand_answer("Q3", answer)

# Step 2 - Score Answer
score = score_answer(structured, "experience")

# Step 3 - Behaviour Analysis
behavior = analyze_behavior(answer)

# Step 4 - Generate Report
report = generate_screening_report(
    candidate["candidate_id"],
    candidate["job_id"],
    [structured],
    [score],
    [behavior]
)

print(report)