from interview_ai.confidence_analyzer import (

    confidence_score,

    detect_hesitation,

    detect_long_pauses
)

from interview_ai.sentiment_engine import (

    analyze_sentiment
)

# -----------------------------------
# Contradiction Detection
# -----------------------------------

def detect_contradiction(text):

    text = text.lower()

    if "yes" in text and "no" in text:

        return True

    return False


# -----------------------------------
# Stress Detection
# -----------------------------------

STRESS_WORDS = [

    "stress",

    "pressure",

    "worried",

    "anxious",

    "nervous"
]


def detect_stress(text):

    text = text.lower()

    return sum(

        text.count(word)

        for word in STRESS_WORDS
    )


# -----------------------------------
# Behavioral Report
# -----------------------------------

def behavioral_report(text):

    confidence = confidence_score(text)

    sentiment = analyze_sentiment(text)

    hesitation = detect_hesitation(text)

    pauses = detect_long_pauses(text)

    contradiction = detect_contradiction(text)

    stress = detect_stress(text)

    return {

        "confidence_score": confidence,

        "sentiment": sentiment["sentiment"],

        "hesitation_count": hesitation["hesitation_count"],

        "repeated_words": hesitation["repeated_words"],

        "long_pauses": pauses,

        "stress_indicator": stress,

        "contradiction": contradiction
    }