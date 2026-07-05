# -----------------------------------
# Conversation States
# -----------------------------------

START = "START"
ASK_QUESTION = "ASK_QUESTION"
FOLLOW_UP = "FOLLOW_UP"
NEXT_QUESTION = "NEXT_QUESTION"
END = "END"


# -----------------------------------
# Follow-up Triggers
# -----------------------------------

def needs_followup(answer):

    if answer.get("is_vague"):

        return True

    if answer.get("off_topic"):

        return True

    if answer.get("confidence_score", 100) < 60:

        return True

    return False


# -----------------------------------
# Get Follow-up Question
# -----------------------------------

def get_followup(question_id):

    followups = {

        "Q1":
            "Could you tell me a little more about yourself?",

        "Q3":
            "Can you explain your previous work experience in more detail?",

        "Q4":
            "Can you describe the projects where you used these skills?"
    }

    return followups.get(

        question_id,

        "Could you please explain further?"
    )


# -----------------------------------
# Decide Next Step
# -----------------------------------

def conversation_step(answer):

    if needs_followup(answer):

        return {

            "state": FOLLOW_UP,

            "question": get_followup(

                answer["question_id"]
            )
        }

    return {

        "state": NEXT_QUESTION
    }

from screening_ai.error_handler import detect_silence

def handle_response(state_machine, answer):

    if detect_silence(answer):

        state_machine.transition("followup")

    else:

        state_machine.transition("next")