SKILL_SYNONYMS = {

    "react.js": "react",
    "nodejs": "node.js",
    "postgres": "postgresql",
    "ml": "machine learning",
    "py": "python"
}

def normalize_skills(skills):

    normalized = []

    for skill in skills:

        if skill in SKILL_SYNONYMS:
            normalized.append(SKILL_SYNONYMS[skill])

        else:
            normalized.append(skill)

    return list(set(normalized))

def normalize_skill(skill):

    skill = skill.lower()

    if skill in SKILL_SYNONYMS:
        return SKILL_SYNONYMS[skill]

    return skill