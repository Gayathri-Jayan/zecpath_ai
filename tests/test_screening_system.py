from screening_ai.answer_understanding_engine import understand_answer
from screening_ai.screening_scorer import score_answer
from screening_ai.confidence_sentiment import analyze_behavior

# -----------------------------------
# Simulated Candidate Responses
# -----------------------------------

TEST_CASES = [

    {
        "question_id": "Q3",
        "answer": "I have 3 years experience in Python and Django.",
        "expected_intent": "experience",
        "human_decision": "Pass"
    },

    {
        "question_id": "Q4",
        "answer": "Maybe I know Java.",
        "expected_intent": "skills",
        "human_decision": "Review"
    },

    {
        "question_id": "Q5",
        "answer": "",
        "expected_intent": "availability",
        "human_decision": "Reject"
    }
]

results = []

for case in TEST_CASES:

    answer = understand_answer(

        case["question_id"],
        case["answer"]
    )

    score = score_answer(

        answer,
        case["expected_intent"]
    )

    behavior = analyze_behavior(

        case["answer"]
    )

    ai_decision = (

        "Pass"

        if score["overall"] >= 80

        else "Review"

        if score["overall"] >= 50

        else "Reject"
    )

    results.append({

        "question_id": case["question_id"],

        "human": case["human_decision"],

        "ai": ai_decision,

        "score": score["overall"]
    })

print(results)