import re

# -------------------------------
# Detect Incomplete Answer
# -------------------------------

def is_incomplete(answer):

    if not answer or len(answer.split()) < 4:
        return True

    return False


# -------------------------------
# Detect Vague Answer
# -------------------------------

VAGUE_WORDS = [

    "maybe",

    "not sure",

    "don't know",

    "probably",

    "i think"
]


def is_vague(answer):

    answer = answer.lower()

    return any(word in answer for word in VAGUE_WORDS)


# -------------------------------
# Detect Confident Answer
# -------------------------------

CONFIDENT_WORDS = [

    "confident",

    "successfully",

    "strong",

    "led",

    "implemented",

    "developed"
]


def is_confident(answer):

    answer = answer.lower()

    return any(word in answer for word in CONFIDENT_WORDS)


# -------------------------------
# Generate Follow-up
# -------------------------------

def generate_followup(question, answer):

    if is_incomplete(answer):

        return {

            "trigger": "clarification",

            "followup":

            "Could you explain that in a little more detail?"
        }

    if is_vague(answer):

        return {

            "trigger": "clarification",

            "followup":

            "Can you be more specific?"
        }

    if is_confident(answer):

        return {

            "trigger": "scenario",

            "followup":

            "Can you give a real example where you applied this?"
        }

    return {

        "trigger": "continue",

        "followup": None
    }