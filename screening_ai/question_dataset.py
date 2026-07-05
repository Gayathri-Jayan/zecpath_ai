# -----------------------------------
# HR Screening Question Dataset
# -----------------------------------

QUESTION_DATASET = [

    {
        "question_id": "Q001",

        "category": "Introduction",

        "question": "Tell me about yourself.",

        "answer_type": "text",

        "mandatory": True,

        "importance": 5,

        "language": "English"
    },

    {
        "question_id": "Q002",

        "category": "Education",

        "question": "What is your highest qualification?",

        "answer_type": "text",

        "mandatory": True,

        "importance": 4,

        "language": "English"
    },

    {
        "question_id": "Q003",

        "category": "Experience",

        "question": "How many years of experience do you have?",

        "answer_type": "number",

        "mandatory": True,

        "importance": 5,

        "language": "English"
    },

    {
        "question_id": "Q004",

        "category": "Skills",

        "question": "Which programming languages are you proficient in?",

        "answer_type": "text",

        "mandatory": True,

        "importance": 5,

        "language": "English"
    },

    {
        "question_id": "Q005",

        "category": "Location",

        "question": "What is your current location?",

        "answer_type": "text",

        "mandatory": False,

        "importance": 3,

        "language": "English"
    },

    {
        "question_id": "Q006",

        "category": "Salary",

        "question": "What is your expected salary?",

        "answer_type": "number",

        "mandatory": False,

        "importance": 2,

        "language": "English"
    },

    {
        "question_id": "Q007",

        "category": "Notice Period",

        "question": "When can you join?",

        "answer_type": "text",

        "mandatory": True,

        "importance": 4,

        "language": "English"
    }
]

# -----------------------------------
# Category Mapping
# -----------------------------------

QUESTION_CATEGORIES = {

    "Introduction": [

        "Tell me about yourself.",

        "Can you briefly introduce yourself?"
    ],

    "Education": [

        "What is your highest qualification?",

        "Which university did you attend?"
    ],

    "Experience": [

        "How many years of experience do you have?",

        "Describe your previous role."
    ],

    "Skills": [

        "Which programming languages are you proficient in?",

        "Have you worked with Django or Flask?"
    ],

    "Location": [

        "What is your current location?",

        "Are you willing to relocate?"
    ],

    "Salary": [

        "What is your current CTC?",

        "What is your expected salary?"
    ],

    "Notice Period": [

        "What is your notice period?",

        "When can you join?"
    ]
}
# -----------------------------------
# Get Questions by Category
# -----------------------------------

def get_questions_by_category(category):

    return [

        q

        for q in QUESTION_DATASET

        if q["category"].lower()

        == category.lower()
    ]


# -----------------------------------
# Get Mandatory Questions
# -----------------------------------

def get_mandatory_questions():

    return [

        q

        for q in QUESTION_DATASET

        if q["mandatory"]
    ]


# -----------------------------------
# Get Questions by Importance
# -----------------------------------

def get_high_priority_questions():

    return [

        q

        for q in QUESTION_DATASET

        if q["importance"] >= 4
    ]

# -----------------------------------
# Reusable Templates
# -----------------------------------

def skill_question(skill):

    return f"Describe your experience with {skill}."


def role_question(role):

    return f"Tell us about your experience working as a {role}."


def technology_question(tech):

    return f"Have you worked with {tech}?"


def education_question(field):

    return f"What degree did you complete in {field}?"

# -----------------------------------
# Generate Screening Flow
# -----------------------------------

def generate_screening_questions():

    questions = []

    categories = [

        "Introduction",

        "Education",

        "Experience",

        "Skills",

        "Location",

        "Salary",

        "Notice Period"
    ]

    for category in categories:

        questions.extend(

            get_questions_by_category(

                category
            )
        )

    return questions

