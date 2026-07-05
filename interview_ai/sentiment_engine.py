POSITIVE = [

    "confident",

    "excellent",

    "good",

    "happy",

    "successful",

    "strong"
]

NEGATIVE = [

    "difficult",

    "bad",

    "weak",

    "stress",

    "problem",

    "failed"
]


def analyze_sentiment(text):

    text = text.lower()

    positive = sum(

        text.count(word)

        for word in POSITIVE
    )

    negative = sum(

        text.count(word)

        for word in NEGATIVE
    )

    if positive > negative:

        sentiment = "Positive"

    elif negative > positive:

        sentiment = "Negative"

    else:

        sentiment = "Neutral"

    return {

        "positive_words": positive,

        "negative_words": negative,

        "sentiment": sentiment
    }