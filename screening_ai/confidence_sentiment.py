import re

# -----------------------------------
# Hesitation Words
# -----------------------------------

HESITATION_WORDS = [

    "um",

    "uh",

    "maybe",

    "perhaps",

    "i think",

    "not sure"
]

# -----------------------------------
# Positive / Negative Words
# -----------------------------------

POSITIVE_WORDS = [

    "confident",

    "excellent",

    "strong",

    "experienced",

    "successful",

    "good"
]

NEGATIVE_WORDS = [

    "weak",

    "difficult",

    "problem",

    "failed",

    "bad",

    "unable"
]


# -----------------------------------
# Hesitation Detection
# -----------------------------------

def detect_hesitation(text):

    text = text.lower()

    count = 0

    for word in HESITATION_WORDS:

        count += text.count(word)

    return count


# -----------------------------------
# Response Length
# -----------------------------------

def response_length(text):

    return len(text.split())


# -----------------------------------
# Response Pace
# -----------------------------------

def response_pace(text):

    words = len(text.split())

    if words >= 20:

        return "Detailed"

    elif words >= 8:

        return "Normal"

    return "Short"


# -----------------------------------
# Uncertainty Detection
# -----------------------------------

def detect_uncertainty(text):

    text = text.lower()

    uncertain = [

        "maybe",

        "not sure",

        "i guess",

        "probably"
    ]

    return any(word in text for word in uncertain)


# -----------------------------------
# Contradiction Detection
# -----------------------------------

def detect_contradiction(text):

    text = text.lower()

    if "yes" in text and "no" in text:

        return True

    return False


# -----------------------------------
# Communication Strength
# -----------------------------------

def communication_strength(text):

    score = 100

    score -= detect_hesitation(text) * 10

    if detect_uncertainty(text):

        score -= 20

    if detect_contradiction(text):

        score -= 20

    return max(score, 0)

# -----------------------------------
# Sentiment Score
# -----------------------------------

def sentiment_score(text):

    text = text.lower()

    positive = 0

    negative = 0

    for word in POSITIVE_WORDS:

        positive += text.count(word)

    for word in NEGATIVE_WORDS:

        negative += text.count(word)

    if positive > negative:

        return "Positive"

    elif negative > positive:

        return "Negative"

    return "Neutral"


# -----------------------------------
# Behavioral Analysis
# -----------------------------------

def analyze_behavior(text):

    return {

        "hesitation_count":

            detect_hesitation(text),

        "response_length":

            response_length(text),

        "response_pace":

            response_pace(text),

        "sentiment":

            sentiment_score(text),

        "uncertainty":

            detect_uncertainty(text),

        "contradiction":

            detect_contradiction(text),

        "communication_strength":

            communication_strength(text)
    }

# -----------------------------------
# Generate Behavioral Report
# -----------------------------------

def generate_behavior_report(text):

    strength = communication_strength(text)

    if strength >= 75:

        level = "Strong"

    elif strength >= 50:

        level = "Moderate"

    else:

        level = "Weak"

    return {

        "confidence": {

            "hesitation_count":
                detect_hesitation(text),

            "response_length":
                response_length(text),

            "response_pace":
                response_pace(text),

            "confidence_score":
                strength
        },

        "sentiment": {

            "sentiment":
                sentiment_score(text)
        },

        "behavior_flags": {

            "uncertainty":
                detect_uncertainty(text),

            "contradiction":
                detect_contradiction(text)
        },

        "communication_strength":
            level
    }

# -----------------------------------
# Compatibility Wrapper (Day 30)
# -----------------------------------

def analyze_response(text):
    """
    Wrapper function for Day 30.
    Returns the behavioral analysis of a response.
    """

    return analyze_behavior(text)