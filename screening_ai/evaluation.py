def calculate_accuracy(results):

    total = len(results)

    correct = 0

    for result in results:

        if result["human"] == result["ai"]:

            correct += 1

    accuracy = (correct / total) * 100

    return round(accuracy, 2)