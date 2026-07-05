import json

from interview_ai.reasoning_scoring import score_reasoning
from interview_ai.scenario_evaluator import evaluate_scenario


# -----------------------------------
# Load Ideal Answer Templates
# -----------------------------------

def load_templates():

    with open(
        "interview_ai/aptitude_answer_templates.json",
        "r"
    ) as file:

        return json.load(file)


# -----------------------------------
# Aptitude Evaluation Pipeline
# -----------------------------------

def evaluate_answer(question_id, answer):

    templates = load_templates()

    # Logical Reasoning Score
    reasoning = score_reasoning(answer)

    # Scenario Evaluation
    if question_id in templates:

        scenario = evaluate_scenario(
            answer,
            templates[question_id]["keywords"]
        )

    else:

        scenario = {
            "scenario_score": 0,
            "matched_keywords": 0,
            "total_keywords": 0
        }

    # Final Score
    final_score = round(
        reasoning * 0.5 +
        scenario["scenario_score"] * 0.5,
        2
    )

    # Aptitude Level
    if final_score >= 85:
        level = "Excellent"

    elif final_score >= 70:
        level = "Good"

    elif final_score >= 50:
        level = "Average"

    else:
        level = "Needs Improvement"

    return {

        "reasoning_score": reasoning,

        "scenario": scenario,

        "final_score": final_score,

        "level": level
    }