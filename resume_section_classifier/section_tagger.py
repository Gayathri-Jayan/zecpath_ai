def clean_sections(sections):

    cleaned = {}

    for section, content in sections.items():

        cleaned[section] = [
            line.strip()
            for line in content
            if line.strip()
        ]

    return cleaned