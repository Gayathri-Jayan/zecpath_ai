def evaluate_scenario(answer, expected_keywords):

    answer = answer.lower()

    matched = 0

    for keyword in expected_keywords:

        if keyword.lower() in answer:

            matched += 1

    score = (matched / len(expected_keywords)) * 100

    return {

        "matched_keywords": matched,

        "total_keywords": len(expected_keywords),

        "scenario_score": round(score, 2)

    }