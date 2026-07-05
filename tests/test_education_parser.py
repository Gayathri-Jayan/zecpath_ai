from ats_engine.education_parser import build_academic_profile


def test_education_parser():

    text = """

    B.Tech Computer Science
    ABC University

    AWS Certification
    """

    result = build_academic_profile(text)

    assert len(result["degrees"]) > 0

    assert len(result["certifications"]) > 0