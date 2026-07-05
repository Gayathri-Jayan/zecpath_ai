# -----------------------------------
# Normalize Score
# -----------------------------------

def normalize_score(score, max_score=10):

    return round((score / max_score) * 100, 2)


# -----------------------------------
# Clarity Score
# -----------------------------------

def score_clarity(answer):

    words = len(answer.split())

    if words >= 10:
        return 9

    elif words >= 5:
        return 7

    return 4


# -----------------------------------
# Relevance Score
# -----------------------------------

def score_relevance(intent, expected_intent):

    if intent == expected_intent:
        return 10

    elif intent == "unknown":
        return 3

    return 6


# -----------------------------------
# Completeness Score
# -----------------------------------

def score_completeness(answer):

    if len(answer.split()) >= 8:
        return 9

    elif len(answer.split()) >= 4:
        return 7

    return 3


# -----------------------------------
# Consistency Score
# -----------------------------------

def score_consistency(is_vague):

    if is_vague:
        return 4

    return 9


# -----------------------------------
# Per-Question Scoring
# -----------------------------------

def score_answer(answer_object, expected_intent):

    clarity = score_clarity(

        answer_object["original_text"]
    )

    relevance = score_relevance(

        answer_object["intent"],

        expected_intent
    )

    completeness = score_completeness(

        answer_object["original_text"]
    )

    consistency = score_consistency(

        answer_object["is_vague"]
    )

    total = (

        clarity +

        relevance +

        completeness +

        consistency

    ) / 4

    return {

        "question_id":

            answer_object["question_id"],

        "clarity":

            normalize_score(clarity),

        "relevance":

            normalize_score(relevance),

        "completeness":

            normalize_score(completeness),

        "consistency":

            normalize_score(consistency),

        "overall":

            normalize_score(total)
    }

# -----------------------------------
# Aggregate Screening Score
# -----------------------------------

def calculate_screening_score(question_scores):

    total = sum(

        score["overall"]

        for score in question_scores
    )

    return round(

        total / len(question_scores),

        2
    )

def generate_screening_result(

        candidate_id,

        question_scores):

    final_score = calculate_screening_score(

        question_scores
    )

    return {

        "candidate_id":

            candidate_id,

        "question_breakdown":

            question_scores,

        "final_screening_score":

            final_score
    }

def calculate_screening_score(question_scores):

    total = sum(
        score["overall"]
        for score in question_scores
    )

    return round(
        total / len(question_scores),
        2
    )

# -----------------------------------
# Explainable Score Output
# -----------------------------------

def generate_screening_result(
        candidate_id,
        question_scores):

    final_score = calculate_screening_score(
        question_scores
    )

    return {

        "candidate_id":
            candidate_id,

        "question_breakdown":
            question_scores,

        "final_screening_score":
            final_score
    }

# -----------------------------------
# Batch Scoring
# -----------------------------------

def score_answers_batch(
        answers,
        expected_intents):

    results = []

    for answer, expected in zip(
            answers,
            expected_intents):

        results.append(

            score_answer(
                answer,
                expected
            )
        )

    return results

