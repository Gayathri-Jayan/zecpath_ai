from screening_ai.answer_understanding_engine import (
    understand_answer,
    extract_entities
)

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