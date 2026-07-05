# -----------------------------------
# Detect Edge Cases
# -----------------------------------

def detect_edge_case(answer):

    if answer is None:

        return "missing_answer"

    answer = answer.strip()

    if answer == "":

        return "missing_answer"

    if "[noise]" in answer.lower():

        return "background_noise"

    if "[poor_audio]" in answer.lower():

        return "poor_audio"

    if "[mixed]" in answer.lower():

        return "language_mixing"

    return "valid"