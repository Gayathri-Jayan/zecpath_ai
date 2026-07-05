from ats_engine.skill_database import TECH_SKILLS

from ats_engine.skill_confidence import calculate_confidence


def extract_skills(text):

    detected_skills = []

    text = text.lower()

    for skill in TECH_SKILLS:

        if skill.lower() in text:

            confidence = calculate_confidence(skill, text)

            detected_skills.append({

                "skill": skill,

                "confidence": confidence
            })

    return detected_skills