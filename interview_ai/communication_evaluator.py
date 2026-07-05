import re

# -----------------------------------
# Filler Words
# -----------------------------------

FILLER_WORDS = [

    "um",

    "uh",

    "like",

    "you know",

    "actually",

    "basically"
]


# -----------------------------------
# Fluency Score
# -----------------------------------

def score_fluency(text):

    words = len(text.split())

    if words >= 25:

        return 100

    elif words >= 15:

        return 80

    elif words >= 8:

        return 60

    return 40


# -----------------------------------
# Grammar Score (Basic Rule-Based)
# -----------------------------------

def score_grammar(text):

    score = 100

    if text.count(".."):

        score -= 10

    if not text.strip().endswith((".", "!", "?")):

        score -= 10

    return max(score, 50)


# -----------------------------------
# Vocabulary Score
# -----------------------------------

def score_vocabulary(text):

    words = text.lower().split()

    unique = len(set(words))

    total = len(words)

    if total == 0:

        return 0

    ratio = unique / total

    return round(ratio * 100)


# -----------------------------------
# Clarity Score
# -----------------------------------

def score_clarity(text):

    sentences = re.split(r"[.!?]", text)

    sentences = [

        s

        for s in sentences

        if s.strip()
    ]

    if len(sentences) == 0:

        return 0

    avg_length = len(text.split()) / len(sentences)

    if avg_length <= 20:

        return 100

    elif avg_length <= 30:

        return 80

    return 60


# -----------------------------------
# Filler Detection
# -----------------------------------

def detect_fillers(text):

    text = text.lower()

    count = 0

    for word in FILLER_WORDS:

        count += text.count(word)

    return count


# -----------------------------------
# Answer Structure
# -----------------------------------

def score_structure(text):

    if len(text.split()) >= 15:

        return 100

    elif len(text.split()) >= 8:

        return 80

    return 60