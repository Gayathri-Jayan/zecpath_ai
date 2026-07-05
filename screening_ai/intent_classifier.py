from screening_ai.answer_understanding_engine import classify_intent

if __name__ == "__main__":

    answer = "I have three years experience in Python and Django"

    result = classify_intent(answer)

    print(result)