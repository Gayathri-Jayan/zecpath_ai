from parsers.resume_extractor import extract_resume

def test_resume_extraction():

    result = extract_resume("data/resumes/Gayathri_Jayan_Resume aurus.pdf")

    assert result["cleaned_text"] != ""