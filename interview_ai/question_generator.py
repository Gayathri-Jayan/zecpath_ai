import json
import random

# -----------------------------------
# Prevent Repeated Questions
# -----------------------------------

ASKED = set()


def ask_question(question):

    if question in ASKED:

        return None

    ASKED.add(question)

    return question


# -----------------------------------
# Load Question Bank
# -----------------------------------

def load_question_bank():

    with open(

        "interview_ai/question_bank.json",

        "r",

        encoding="utf-8"

    ) as file:

        return json.load(file)


# -----------------------------------
# Generate Role-Based Questions
# -----------------------------------

def generate_questions(

        role_type,

        experience_level,

        max_questions=6):

    qb = load_question_bank()

    questions = []

    # Introduction Questions

    questions += qb["categories"]["introduction"][

        experience_level

    ]

    # Common HR Categories

    for category in [

        "strengths_weaknesses",

        "teamwork",

        "career_goals",

        "availability"

    ]:

        questions += qb["categories"][

            category

        ]["common"]

    # Role-Based Questions

    questions += qb["role_based"][

        role_type

    ]

    # Remove duplicate questions

    questions = list(

        dict.fromkeys(questions)

    )

    # Remove already asked questions

    questions = [

        q for q in questions

        if q not in ASKED

    ]

    if not questions:

        return []

    return random.sample(

        questions,

        min(max_questions, len(questions))
    )


# -----------------------------------
# Get Available Categories
# -----------------------------------

def get_question_categories():

    qb = load_question_bank()

    return list(

        qb["categories"].keys()
    )


# -----------------------------------
# Remove Repeated Questions
# -----------------------------------

def remove_repeated_questions(

        questions,

        asked_questions):

    return [

        question

        for question in questions

        if question not in asked_questions
    ]


# -----------------------------------
# Reset Question History
# -----------------------------------

def reset_question_history():

    ASKED.clear()


# -----------------------------------
# Example Execution
# -----------------------------------

if __name__ == "__main__":

    questions = generate_questions(

        role_type="technical",

        experience_level="fresher"

    )

    print("Generated Questions:\n")

    for question in questions:

        print("-", ask_question(question))