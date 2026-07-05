from resume_section_classifier.section_parser import parse_resume_sections

def test_sections():

    sample = """

    Skills
    Python
    Flask

    Education
    B.Tech
    """

    result = parse_resume_sections(sample)

    assert "skills" in result