from screening_ai.transcript_processor import (
    process_transcript
)


def test_processor():

    text = "Um I have three years experience in Python"

    result = process_transcript(

        text
    )

    print(result)

    assert result["status"] == "processed"


test_processor()