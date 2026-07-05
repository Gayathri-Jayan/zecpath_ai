from ats_engine.experience_parser import extract_experience_blocks

def test_experience_parser():

    text = "ABC Tech (2021–2024)"

    result = extract_experience_blocks(text)

    assert len(result) > 0

    assert result[0]["duration_years"] == 3