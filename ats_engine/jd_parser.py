import re

from ats_engine.skill_matcher import extract_skills
from ats_engine.role_detector import detect_role
from ats_engine.experience_parser import extract_experience
from ats_engine.education_parser import extract_education
from ats_engine.skill_synonyms import normalize_skills

from loguru import logger

logger.add("logs/jd_parser.log")

def clean_jd_text(text):

    text = text.lower()

    text = re.sub(r'\s+', ' ', text)

    text = re.sub(r'[^\w\s+#.-]', ' ', text)

    return text.strip()

def build_jd_profile(text):
    logger.info("JD parsing started")

    cleaned_text = clean_jd_text(text)

    normalized_text = cleaned_text

    for key, value in {
        "react.js": "react",
        "nodejs": "node.js",
        "ml": "machine learning",
        "py": "python"
    }.items():

        normalized_text = normalized_text.replace(key, value)

    skills = extract_skills(normalized_text)

    jd_profile = {

        "role": detect_role(cleaned_text),

        "required_skills": skills,

        "experience_required":
            extract_experience(cleaned_text),

        "education_required":
            extract_education(cleaned_text),

        "cleaned_text": cleaned_text
    }

    logger.success("JD parsed successfully")

    return jd_profile