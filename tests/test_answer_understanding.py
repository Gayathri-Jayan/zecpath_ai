from screening_ai.answer_understanding_engine import (
    understand_answer,
    extract_entities
)

answer = "I have 3 years experience in Python and Django and can join immediately"

print(

    understand_answer(

        "Q3",

        answer
    )
)

print(

    extract_entities(

        answer
    )
)