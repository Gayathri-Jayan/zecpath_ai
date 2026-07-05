from interview_ai.hr_scoring_engine import calculate_hr_score


def generate_hr_report(

        candidate_id,

        answer,

        relevance_score):

    score = calculate_hr_score(

        answer,

        relevance_score
    )

    if score["final_hr_score"] >= 85:

        decision = "Excellent"

    elif score["final_hr_score"] >= 70:

        decision = "Good"

    elif score["final_hr_score"] >= 50:

        decision = "Average"

    else:

        decision = "Poor"

    return {

        "candidate_id":

            candidate_id,

        "score_breakdown":

            score,

        "overall_rating":

            decision
    }