SKILLS = [
    "python",
    "java",
    "react",
    "node.js",
    "mongodb",
    "sql",
    "docker",
    "aws",
    "machine learning",
    "flask"
]

def extract_skills(text):

    detected_skills = []

    for skill in SKILLS:

        if skill.lower() in text.lower():
            detected_skills.append(skill)

    return list(set(detected_skills))