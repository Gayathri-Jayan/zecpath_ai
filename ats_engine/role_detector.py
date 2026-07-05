ROLES = [
    "mern stack developer",
    "python developer",
    "data analyst",
    "ui ux designer",
    "devops engineer",
    "sales executive"
]

def detect_role(text):

    for role in ROLES:

        if role in text.lower():
            return role

    return "unknown"

# -----------------------------------
# Rank Candidates
# -----------------------------------

def rank_candidates(candidates):

    """
    Sort candidates based on final_score
    """

    ranked = sorted(

        candidates,

        key=lambda x: x.get(
            "final_score",
            0
        ),

        reverse=True
    )

    # Assign Rank

    for idx, candidate in enumerate(

        ranked,

        start=1
    ):

        candidate["rank"] = idx

    return ranked


# -----------------------------------
# Threshold Configuration
# -----------------------------------

THRESHOLDS = {

    "shortlist": 75,

    "review": 50
}


# -----------------------------------
# Candidate Classification
# -----------------------------------

def classify_candidate(score):

    if score >= THRESHOLDS["shortlist"]:

        return "Shortlisted"

    elif score >= THRESHOLDS["review"]:

        return "Review"

    else:

        return "Rejected"


# -----------------------------------
# Apply Shortlisting
# -----------------------------------

def apply_shortlisting(candidates):

    for candidate in candidates:

        score = candidate.get(

            "final_score",

            0
        )

        candidate["status"] = classify_candidate(

            score
        )

    return candidates


# -----------------------------------
# Top Candidate Selector
# -----------------------------------

def get_top_candidates(

    candidates,

    top_n=5
):

    return candidates[:top_n]


# -----------------------------------
# Complete Ranking Pipeline
# -----------------------------------

def ranking_pipeline(candidates):

    ranked = rank_candidates(candidates)

    shortlisted = apply_shortlisting(ranked)

    top_candidates = get_top_candidates(

        shortlisted
    )

    return {

        "ranked_list": shortlisted,

        "top_candidates": top_candidates
    }