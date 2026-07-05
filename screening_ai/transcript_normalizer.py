import re


def normalize_transcript(text):

    text = text.lower()

    text = re.sub(

        r"[^a-z0-9\s\.\,\-]",

        "",

        text
    )

    text = re.sub(

        r"\s+",

        " ",

        text
    )

    return text.strip()
import re


def normalize_transcript(text):

    text = text.lower()

    fillers = [

        "um",

        "uh",

        "like",

        "you know"
    ]

    for f in fillers:

        text = re.sub(

            rf"\b{f}\b",

            "",

            text
        )

    text = re.sub(

        r"\s+",

        " ",

        text
    )

    return text.strip()

if __name__ == "__main__":

    text = "Um I have three years experience"

    result = normalize_transcript(text)

    print(result)