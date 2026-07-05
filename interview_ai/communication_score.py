from interview_ai.communication_evaluator import (

    score_fluency,

    score_grammar,

    score_vocabulary,

    score_clarity,

    detect_fillers,

    score_structure
)


# -----------------------------------
# Communication Score
# -----------------------------------

def communication_score(text):

    fluency = score_fluency(text)

    grammar = score_grammar(text)

    vocabulary = score_vocabulary(text)

    clarity = score_clarity(text)

    structure = score_structure(text)

    fillers = detect_fillers(text)

    filler_penalty = min(fillers * 5, 20)

    final = (

        fluency * 0.25 +

        grammar * 0.20 +

        vocabulary * 0.15 +

        clarity * 0.20 +

        structure * 0.20

    )

    final -= filler_penalty

    final = max(final, 0)

    final_score = round(final, 2)

    return {

        "communication_score": final_score,

        "normalized_score": normalize_score(final_score),

        "level": get_score_level(final_score),

        "breakdown": {

            "fluency": round(fluency, 2),

            "grammar": round(grammar, 2),

            "vocabulary": round(vocabulary, 2),

            "clarity": round(clarity, 2),

            "structure": round(structure, 2),

            "filler_words": fillers,

            "penalty": filler_penalty
        }
    }

    # return {

    #     "fluency": fluency,

    #     "grammar": grammar,

    #     "vocabulary": vocabulary,

    #     "clarity": clarity,

    #     "structure": structure,

    #     "filler_words": fillers,

    #     "communication_score":

    #         round(final, 2)
    # }


# -----------------------------------
# Communication Level
# -----------------------------------

def get_score_level(score):

    if score >= 85:

        return "Excellent"

    elif score >= 70:

        return "Good"

    elif score >= 50:

        return "Average"

    return "Poor"

# -----------------------------------
# Bias Normalization
# -----------------------------------

def normalize_score(score):

    return round(

        min(max(score, 0), 100),

        2
    )