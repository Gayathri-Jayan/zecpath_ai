def calculate_confidence(skill, text):

    occurrences = text.lower().count(skill.lower())

    if occurrences >= 3:
        return 0.95

    elif occurrences == 2:
        return 0.85

    elif occurrences == 1:
        return 0.70

    return 0.0