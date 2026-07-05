from ats_engine.ats_scorer import calculate_score

def test_ats_score():
    score = calculate_score(["Python", "React"])
    assert score >= 0

