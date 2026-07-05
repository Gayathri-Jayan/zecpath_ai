import re

# -----------------------------------
# Filler Words
# -----------------------------------

FILLER_WORDS = [

    "um",

    "uh",

    "like",

    "you know",

    "actually"
]


# -----------------------------------
# Clean Transcript
# -----------------------------------

def clean_transcript(text):

    text = text.lower()

    # Remove filler words

    for word in FILLER_WORDS:

        text = re.sub(

            rf"\b{word}\b",

            "",

            text
        )

    # Remove repeated spaces

    text = re.sub(

        r"\s+",

        " ",

        text
    )

    # Remove repeated punctuation

    text = re.sub(

        r"[.,!?]{2,}",

        ".",

        text
    )

    return text.strip()


# -----------------------------------
# Handle Partial Answers
# -----------------------------------

def handle_partial_answer(text):

    if len(text.split()) < 3:

        return "PARTIAL_ANSWER"

    return text


# -----------------------------------
# Silence Detection
# -----------------------------------

def detect_silence(text):

    if text.strip() == "":

        return True

    return False


# -----------------------------------
# Complete Pipeline
# -----------------------------------

def process_transcript(text):

    if detect_silence(text):

        return {

            "status": "silence_detected"
        }

    text = clean_transcript(text)

    text = handle_partial_answer(text)

    return {

        "status": "processed",

        "clean_text": text
    }

if __name__ == "__main__":

    text = "Um I have three years experience in Python"

    result = process_transcript(text)

    print(result)