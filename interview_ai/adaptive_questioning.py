from interview_ai.followup_engine import (

    is_confident,

    is_incomplete,

    is_vague
)


def choose_next_question(answer):

    if is_incomplete(answer):

        return "Please explain your previous answer."

    if is_vague(answer):

        return "Can you provide more specific details?"

    if is_confident(answer):

        return "Describe a real-world situation where you used this skill."

    return "Proceed to the next HR question."