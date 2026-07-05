from resume_section_classifier.section_rules import SECTION_HEADERS

def detect_heading(line):

    line = line.strip().lower()

    for section, headings in SECTION_HEADERS.items():

        if line in headings:
            return section

    return None