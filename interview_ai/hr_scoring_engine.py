from interview_ai.communication_score import communication_score
from interview_ai.behavioral_signals import behavioral_report


# -----------------------------------
# Weight Configuration
# -----------------------------------

WEIGHTS = {

    "answer_relevance": 0.40,

    "communication": 0.25,

    "confidence": 0.20,

    "consistency": 0.15
}


# -----------------------------------
# Consistency Score
# -----------------------------------

def score_consistency(answer):

    if "not sure" in answer.lower():

        return 60

    if len(answer.split()) < 4:

        return 70

    return 100


# -----------------------------------
# HR Interview Score
# -----------------------------------

def calculate_hr_score(

        answer,

        relevance_score):

    communication = communication_score(answer)

    behavior = behavioral_report(answer)

    consistency = score_consistency(answer)

    final = (

        relevance_score * WEIGHTS["answer_relevance"]

        +

        communication["communication_score"]

        * WEIGHTS["communication"]

        +

        behavior["confidence_score"]

        * WEIGHTS["confidence"]

        +

        consistency

        * WEIGHTS["consistency"]

    )

    return {

        "answer_relevance":

            relevance_score,

        "communication_score":

            communication["communication_score"],

        "confidence_score":

            behavior["confidence_score"],

        "consistency_score":

            consistency,

        "final_hr_score":

            round(final, 2)
    }


# -----------------------------------
# Normalize Score
# -----------------------------------

def normalize_hr_score(

        score,

        max_score=100):

    return round(

        (score / max_score) * 100,

        2
    )