from screening_ai.question_dataset import (
    generate_screening_questions,
    get_mandatory_questions
)

questions = generate_screening_questions()

print("Total Questions:", len(questions))

print()

for q in questions:

    print(q)

print()

mandatory = get_mandatory_questions()

print("Mandatory Questions:")

for q in mandatory:

    print(q)