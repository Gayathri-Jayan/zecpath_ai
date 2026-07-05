import re

# -----------------------------------
# Intent Keywords
# -----------------------------------

INTENT_KEYWORDS = {

    "skills": [
        "python",
        "java",
        "react",
        "django",
        "sql"
    ],

    "experience": [
        "year",
        "experience",
        "worked",
        "intern"
    ],

    "availability": [
        "immediate",
        "notice period",
        "join"
    ],

    "salary": [
        "salary",
        "ctc",
        "lpa",
        "package"
    ]
}


# -----------------------------------
# Intent Classification
# -----------------------------------

def classify_intent(answer):

    answer = answer.lower()

    for intent, keywords in INTENT_KEYWORDS.items():

        for keyword in keywords:

            if keyword in answer:

                return intent

    return "unknown"


# -----------------------------------
# Off-topic Detection
# -----------------------------------

def detect_off_topic(answer):

    if len(answer.split()) < 2:

        return True

    return False


# -----------------------------------
# Missing / Vague Answer Detection
# -----------------------------------

def detect_vague_answer(answer):

    vague_words = [

        "maybe",

        "not sure",

        "don't know",

        "none"
    ]

    answer = answer.lower()

    return any(word in answer for word in vague_words)


# -----------------------------------
# Structured Answer Object
# -----------------------------------

def understand_answer(question_id, answer):

    return {

        "question_id": question_id,

        "answer": answer,
        "original_text": answer,

        "intent": classify_intent(answer),

        "off_topic": detect_off_topic(answer),
        "is_vague": detect_vague_answer(answer),

        "vague_answer": detect_vague_answer(answer),
        "skills": extract_entities(answer)["skills"],

        "experience_years": extract_entities(answer)["experience"] or 0,

        "availability": extract_entities(answer)["availability"] or "Unknown",

        "salary": extract_entities(answer)["salary"]
    }

# -----------------------------------
# Entity Extraction
# -----------------------------------

def extract_entities(answer):

    answer = answer.lower()

    entities = {

        "skills": [],

        "experience": None,

        "availability": None,

        "salary": None
    }

    skills_db = [

        "python",

        "java",

        "django",

        "react",

        "sql"
    ]

    for skill in skills_db:

        if skill in answer:

            entities["skills"].append(skill)

    exp_match = re.search(r"(\d+)\s+year", answer)

    if exp_match:

        entities["experience"] = int(exp_match.group(1))

    if "immediate" in answer:

        entities["availability"] = "immediate"

    salary_match = re.search(r"(\d+)\s*lpa", answer)

    if salary_match:

        entities["salary"] = salary_match.group(1) + " LPA"

    return entities
# -----------------------------------
# Individual Extractors
# -----------------------------------

def extract_skills(answer):

    return extract_entities(answer)["skills"]


def extract_experience(answer):

    exp = extract_entities(answer)["experience"]

    return exp if exp else 0


def extract_salary(answer):

    return extract_entities(answer)["salary"]


def extract_availability(answer):

    availability = extract_entities(answer)["availability"]

    return availability if availability else "Unknown"


# -----------------------------------
# Off-topic Detection
# -----------------------------------

def is_off_topic(intent):

    return intent == "unknown"


# -----------------------------------
# Vague Answer Detection
# -----------------------------------

def is_vague(answer):

    return detect_vague_answer(answer)


# -----------------------------------
# Main Answer Processing
# -----------------------------------

def process_answer(question_id, answer_text):

    intent = classify_intent(answer_text)

    structured = {

        "question_id": question_id,

        "original_text": answer_text,

        "intent": intent,

        "skills": extract_skills(answer_text),

        "experience_years": extract_experience(answer_text),

        "salary": extract_salary(answer_text),

        "availability": extract_availability(answer_text),

        "off_topic": is_off_topic(intent),

        "is_vague": is_vague(answer_text)
    }

    return structured

if __name__ == "__main__":

    answer = "I have three years experience in Python and Django"

    semantic_object = {

        "candidate_id": "C123",

        "question_id": "Q3",

        "answer": answer,

        "intent": understand_answer(
            "Q3",
            answer
        )["intent"],

        "entities": extract_entities(
            answer
        ),

        "off_topic": understand_answer(
            "Q3",
            answer
        )["off_topic"],

        "vague_answer": understand_answer(
            "Q3",
            answer
        )["vague_answer"]
    }

    print(semantic_object)