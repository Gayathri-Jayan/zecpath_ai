# -----------------------------------
# Silence Detection
# -----------------------------------

def detect_silence(answer):

    return len(answer.strip()) == 0


# -----------------------------------
# Repeated Answer Detection
# -----------------------------------

def repeated_answer(current, previous):

    return current.strip().lower() == previous.strip().lower()


# -----------------------------------
# Retry Logic
# -----------------------------------

def retry_message():

    return "I'm sorry, I didn't catch that. Could you please repeat your answer?"


# -----------------------------------
# Confusion Handling
# -----------------------------------

def confusion_message():

    return "Let me rephrase the question."


# -----------------------------------
# Failure Handling
# -----------------------------------

def failure_message():

    return "We'll move to the next question."

RETRY_MESSAGES = {

    "silence":
        "Sorry, I didn't hear anything. Could you please respond?",

    "confusion":
        "Let me clarify the question for you.",

    "repeat":
        "Could you provide more details?"
}