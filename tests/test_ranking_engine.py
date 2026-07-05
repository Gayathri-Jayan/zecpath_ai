# -----------------------------------
# Rank Candidates
# -----------------------------------

def rank_candidates(candidates):

    ranked = sorted(

        candidates,

        key=lambda x: x.get(
            "final_score",
            0
        ),

        reverse=True
    )

    for idx, candidate in enumerate(

        ranked,

        start=1
    ):

        candidate["rank"] = idx

    return ranked


# -----------------------------------
# Thresholds
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
# Ranking Pipeline
# -----------------------------------

def ranking_pipeline(candidates):

    ranked = rank_candidates(
        candidates
    )

    shortlisted = apply_shortlisting(
        ranked
    )

    top_candidates = get_top_candidates(
        shortlisted
    )

    return {

        "ranked_list": shortlisted,

        "top_candidates": top_candidates
    }

from ats_engine.ranking_engine import ranking_pipeline

candidates = [
    {"candidate_id": "C1", "final_score": 88},
    {"candidate_id": "C2", "final_score": 72},
    {"candidate_id": "C3", "final_score": 45},
    {"candidate_id": "C4", "final_score": 80}
]

result = ranking_pipeline(candidates)

print(result)