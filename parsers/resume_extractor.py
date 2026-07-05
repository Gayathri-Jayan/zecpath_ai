import os

from parsers.pdf_reader import extract_pdf_text
from parsers.docx_reader import extract_docx_text
from parsers.text_cleaner import clean_text

from resume_section_classifier.section_parser import parse_resume_sections
from resume_section_classifier.section_tagger import clean_sections
from resume_section_classifier.layout_handler import normalize_layout

from ats_engine.skill_extractor import extract_skills

from ats_engine.experience_parser import (
    extract_experience_blocks,
    extract_roles,
    calculate_total_experience,
    detect_gaps,
    detect_overlaps,
    calculate_relevance
)

from ats_engine.education_parser import build_academic_profile

from parsers.normalization import (
    normalize_resume_text
)

# -----------------------------------
# Main Resume Extraction Function
# -----------------------------------

def extract_resume(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    # -----------------------------------
    # Extract Raw Text
    # -----------------------------------

    if ext == ".pdf":

        raw_text = extract_pdf_text(file_path)

    elif ext == ".docx":

        raw_text = extract_docx_text(file_path)

    else:
        raise ValueError("Unsupported file format")

    # -----------------------------------
    # Clean & Normalize Text
    # -----------------------------------

    cleaned_text = clean_text(raw_text)

    cleaned_text = normalize_resume_text(
        cleaned_text
    )

    cleaned_text = normalize_layout(cleaned_text)

    # -----------------------------------
    # Resume Section Segmentation
    # -----------------------------------

    sections = parse_resume_sections(cleaned_text)

    sections = clean_sections(sections)

    # -----------------------------------
    # Skill Extraction
    # -----------------------------------

    skills = extract_skills(cleaned_text)

    # -----------------------------------
    # Experience Parsing
    # -----------------------------------

    experiences = extract_experience_blocks(raw_text)

    roles = extract_roles(raw_text)

    total_experience = calculate_total_experience(
        experiences
    )

    academic_profile = build_academic_profile(
        raw_text
    )

    gaps = detect_gaps(experiences)

    overlaps = detect_overlaps(experiences)

    relevance_score = calculate_relevance(
        roles,
        "developer"
    )

    # -----------------------------------
    # Final Structured Output
    # -----------------------------------

    return {

        "raw_text": raw_text,

        "cleaned_text": cleaned_text,

        "sections": sections,

        "skills": skills,

        "experience": {

            "experiences": experiences,

            "roles": roles,

            "total_experience": total_experience,

            "gaps": gaps,

            "overlaps": overlaps,
            "academic_profile": academic_profile,

            "relevance_score": relevance_score
        }
    }


# -----------------------------------
# Save Extracted Text Files
# -----------------------------------

def save_text_outputs(file_name, raw_text, cleaned_text):

    base_name = os.path.splitext(file_name)[0]

    raw_path = f"data/extracted_text/{base_name}.txt"

    cleaned_path = f"data/cleaned_resumes/{base_name}.txt"

    with open(raw_path, "w", encoding="utf-8") as f:

        f.write(raw_text)

    with open(cleaned_path, "w", encoding="utf-8") as f:

        f.write(cleaned_text)