import re

from datetime import datetime


# -----------------------------------
# Extract Experience Blocks
# -----------------------------------


def extract_experience_blocks(text):

    experiences = []

    pattern = r'([A-Za-z0-9\s.,&\-]+)\n([A-Za-z]{3,9}\s\d{1,2},\s\d{4})\s[–-]\s([A-Za-z]{3,9}\s\d{1,2},\s\d{4}|Present)'

    matches = re.findall(pattern, text)

    for match in matches:

        company = match[0].strip()

        start_date = match[1]

        end_date = match[2]

        start_year = int(re.search(r'\d{4}', start_date).group())

        if end_date.lower() == "present":

            end_year = datetime.now().year

        else:

            end_year = int(re.search(r'\d{4}', end_date).group())

        duration = end_year - start_year

        experiences.append({

            "company": company,

            "start_year": start_year,

            "end_year": end_year,

            "duration_years": duration
        })

    return experiences

# -----------------------------------
# Extract Roles
# -----------------------------------

def extract_roles(text):

    roles = [
        "developer",
        "engineer",
        "manager",
        "analyst",
        "intern"
    ]

    found_roles = []

    for role in roles:

        if role in text.lower():

            found_roles.append(role)

    return list(set(found_roles))


# -----------------------------------
# Calculate Total Experience
# -----------------------------------

def calculate_total_experience(experiences):

    total = sum([
        exp["duration_years"]
        for exp in experiences
    ])

    return total


# -----------------------------------
# Gap Detection
# -----------------------------------

def detect_gaps(experiences):

    gaps = []

    sorted_exp = sorted(
        experiences,
        key=lambda x: x["start_year"]
    )

    for i in range(1, len(sorted_exp)):

        prev_end = sorted_exp[i - 1]["end_year"]

        curr_start = sorted_exp[i]["start_year"]

        if curr_start > prev_end:

            gaps.append({

                "gap_years": curr_start - prev_end,

                "between": f"{prev_end} - {curr_start}"
            })

    return gaps


# -----------------------------------
# Overlap Detection
# -----------------------------------

def detect_overlaps(experiences):

    overlaps = []

    for i in range(len(experiences)):

        for j in range(i + 1, len(experiences)):

            if experiences[i]["end_year"] > experiences[j]["start_year"]:

                overlaps.append((

                    experiences[i],

                    experiences[j]
                ))

    return overlaps


# -----------------------------------
# Role Similarity Mapping
# -----------------------------------

ROLE_SIMILARITY = {

    "developer": [
        "engineer",
        "programmer"
    ],

    "engineer": [
        "developer"
    ],

    "analyst": [
        "data analyst",
        "business analyst"
    ],

    "manager": [
        "team lead",
        "project manager"
    ]
}


# -----------------------------------
# Relevance Scoring
# -----------------------------------

def calculate_relevance(candidate_roles, job_role):

    score = 0

    for role in candidate_roles:

        if role == job_role:

            score += 1

        elif role in ROLE_SIMILARITY.get(job_role, []):

            score += 0.7

    if len(candidate_roles) == 0:

        return 0

    return round((score / len(candidate_roles)) * 100, 2)