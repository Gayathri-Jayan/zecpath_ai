def score_reasoning(answer):

    answer = answer.lower()

    score = 0

    keywords = [

        "because",

        "therefore",

        "reason",

        "logic",

        "solution",

        "analysis"

    ]

    for word in keywords:

        if word in answer:

            score += 15

    score += min(len(answer.split()), 10)

    return min(score, 100)