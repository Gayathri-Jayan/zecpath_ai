from ats_engine.jd_parser import build_jd_profile

def test_jd_parser():

    sample_jd = """

    Looking for Python Developer
    with 3+ years experience in Flask,
    SQL and AWS.

    """

    result = build_jd_profile(sample_jd)

    assert result["role"] != "unknown"