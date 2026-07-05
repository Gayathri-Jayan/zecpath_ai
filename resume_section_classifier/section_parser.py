from resume_section_classifier.heading_detector import detect_heading

def parse_resume_sections(text):

    lines = text.split("\n")

    sections = {}

    current_section = "other"

    sections[current_section] = []

    for line in lines:

        cleaned_line = line.strip()

        if not cleaned_line:
            continue

        detected = detect_heading(cleaned_line)

        if detected:

            current_section = detected

            if current_section not in sections:
                sections[current_section] = []

        else:

            sections[current_section].append(cleaned_line)

    return sections