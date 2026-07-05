def calculate_relevance(candidate_roles, target_role):

    score = 0

    for role in candidate_roles:

        if role == target_role:
            score += 1

    return score / len(candidate_roles)