import spacy

nlp = spacy.load("en_core_web_sm")

SECTION_KEYWORDS = {

    "skills": [
        "python",
        "java",
        "react",
        "sql",
        "aws"
    ],

    "education": [
        "b.tech",
        "mca",
        "university",
        "cgpa"
    ],

    "experience": [
        "worked",
        "company",
        "developer",
        "intern"
    ]
}

def classify_section(text):

    text = text.lower()

    scores = {}

    for section, keywords in SECTION_KEYWORDS.items():

        scores[section] = 0

        for word in keywords:

            if word in text:
                scores[section] += 1

    if scores:
        return max(scores, key=scores.get)

    return "other"