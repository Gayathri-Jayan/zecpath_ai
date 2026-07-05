from screening_ai.answer_understanding_engine import process_answer

from screening_ai.screening_scorer import (
    score_answer,
    generate_screening_result
)

answer = process_answer(
    "Q3",
    "I have 3 years experience in Python and Django"
)

score = score_answer(
    answer,
    "experience"
)

print(score)

result = generate_screening_result(
    "C123",
    [score]
)

print(result)