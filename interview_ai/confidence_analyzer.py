import re

# -----------------------------------
# Uncertainty Words
# -----------------------------------

UNCERTAINTY_WORDS = [

    "maybe",

    "perhaps",

    "i think",

    "not sure",

    "probably",

    "guess"
]

# -----------------------------------
# Detect Hesitation
# -----------------------------------

def detect_hesitation(text):

    text = text.lower()

    hesitation = sum(

        text.count(word)

        for word in UNCERTAINTY_WORDS
    )

    repeated = len(

        re.findall(

            r"\b(\w+)\s+\1\b",

            text
        )
    )

    return {

        "hesitation_count": hesitation,

        "repeated_words": repeated
    }


# -----------------------------------
# Long Pause Detection
# -----------------------------------

def detect_long_pauses(text):

    pauses = text.count("...")

    return pauses


# -----------------------------------
# Confidence Score
# -----------------------------------

def confidence_score(text):

    hesitation = detect_hesitation(text)

    pauses = detect_long_pauses(text)

    score = 100

    score -= hesitation["hesitation_count"] * 10

    score -= hesitation["repeated_words"] * 5

    score -= pauses * 10

    return max(score, 0)