# -----------------------------------
# Interview Summary Generator
# -----------------------------------

def generate_interview_summary(candidate):

    strengths = []
    weaknesses = []
    cultural_fit = []
    risks = []
    inconsistencies = []

    # Strengths
    if candidate.get("communication_score", 0) >= 80:
        strengths.append("Strong communication skills")

    if candidate.get("confidence_score", 0) >= 80:
        strengths.append("High confidence during interview")

    if candidate.get("aptitude_score", 0) >= 75:
        strengths.append("Good logical reasoning ability")

    # Weaknesses
    if candidate.get("communication_score", 0) < 60:
        weaknesses.append("Communication needs improvement")

    if candidate.get("confidence_score", 0) < 60:
        weaknesses.append("Low confidence observed")

    # Cultural Fit
    if candidate.get("teamwork", False):
        cultural_fit.append("Shows collaborative mindset")

    if candidate.get("adaptability", False):
        cultural_fit.append("Adaptable to new environments")

    # Risk Flags
    if candidate.get("stress_score", 1.0) < 0.5:
        risks.append("High stress indicators detected")

    if candidate.get("contradiction", False):
        risks.append("Contradictory responses identified")

    # Inconsistencies
    if candidate.get("is_vague", False):
        inconsistencies.append("Some answers lacked clarity")

    overall = (
        "Candidate performed well overall and demonstrated good communication, "
        "reasoning ability, and confidence."
    )

    return {

        "candidate_id": candidate["candidate_id"],

        "strengths": strengths,

        "weaknesses": weaknesses,

        "cultural_fit": cultural_fit,

        "risk_flags": risks,

        "inconsistencies": inconsistencies,

        "overall_summary": overall
    }