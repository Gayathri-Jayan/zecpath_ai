INTERVIEW_STATE = {

    "question_id": None,

    "question": None,

    "candidate_response": None,

    "follow_up_allowed": True,

    "current_phase": "Introduction"
}

INTERVIEW_PROGRESS = {

    "current_question": 1,

    "questions_asked": [],

    "followups_given": [],

    "visited_questions": set(),
    
}


def update_state(

        question_id,

        followup=False):

    INTERVIEW_PROGRESS["questions_asked"].append(

        question_id
    )

    if followup:

        INTERVIEW_PROGRESS["followups_given"].append(

            question_id
        )

    INTERVIEW_PROGRESS["visited_questions"].add(

        question_id
    )

    INTERVIEW_PROGRESS["current_question"] += 1
