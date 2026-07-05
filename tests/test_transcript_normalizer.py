from screening_ai.transcript_normalizer import (
    normalize_transcript
)


def test_normalizer():

    text = "I have THREE Years of Experience!!!"

    result = normalize_transcript(

        text
    )

    print(result)

    assert result == "i have three years of experience"


test_normalizer()