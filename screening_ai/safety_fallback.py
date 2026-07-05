# -----------------------------------
# Safety Fallback Messages
# -----------------------------------

FALLBACK_MESSAGES = {

    "poor_audio":
        "The audio quality is poor. Could you please repeat your answer?",

    "background_noise":
        "There seems to be background noise. Please speak clearly.",

    "language_mixing":
        "Please answer in a single language for better understanding.",

    "missing_answer":
        "No response detected. Could you please answer the question?"
}


def get_fallback_response(issue):

    return FALLBACK_MESSAGES.get(

        issue,

        "Please try again."
    )