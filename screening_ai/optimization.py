# -----------------------------------
# Intent Threshold
# -----------------------------------

INTENT_THRESHOLD = 0.65


# -----------------------------------
# Screening Thresholds
# -----------------------------------

PASS_SCORE = 75

REVIEW_SCORE = 55


# -----------------------------------
# Decision
# -----------------------------------

def screening_decision(score):

    if score >= PASS_SCORE:

        return "Pass"

    elif score >= REVIEW_SCORE:

        return "Review"

    return "Reject"


# -----------------------------------
# Reduce False Rejections
# -----------------------------------

def reduce_false_rejection(score, confidence):

    if score >= REVIEW_SCORE and confidence > 80:

        return "Review"

    return screening_decision(score)