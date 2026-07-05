from interview_ai.hr_scoring_engine import calculate_hr_score


# -----------------------------------
# Simulate Single Interview
# -----------------------------------

def simulate_interview(candidate):

    result = calculate_hr_score(

        answer=candidate["answer"],

        relevance_score=candidate["relevance_score"]

    )

    final_score = result["final_hr_score"]

    if final_score >= 75:

        ai_decision = "Strong Hire"

    elif final_score >= 55:

        ai_decision = "Consider"

    else:

        ai_decision = "Reject"

    return {

        "candidate_name": candidate["candidate_name"],

        "candidate_type": candidate["candidate_type"],

        "manual_decision": candidate["manual_decision"],

        "ai_decision": ai_decision,

        "hr_score": final_score
    }


# -----------------------------------
# Simulate Multiple Interviews
# -----------------------------------

def simulate_multiple(candidates):

    results = []

    for candidate in candidates:

        results.append(

            simulate_interview(candidate)

        )

    return results