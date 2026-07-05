from interview_ai.communication_score import communication_score

answer = (

    "I am confident in Python development. "

    "I have worked on Django and REST APIs "

    "and successfully delivered multiple projects."

)


result = communication_score(answer)
assert result["communication_score"] >= 0

assert result["level"] in [

    "Excellent",

    "Good",

    "Average",

    "Poor"
]

print(result)