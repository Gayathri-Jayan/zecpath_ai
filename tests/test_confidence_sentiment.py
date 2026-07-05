from screening_ai.confidence_sentiment import analyze_behavior
from screening_ai.confidence_sentiment import generate_behavior_report

text = """
I am confident in Python.
I have three years experience.
"""

result = analyze_behavior(text)

print(result)

assert result["communication_strength"] > 50

assert result["sentiment"] == "Positive"

result = generate_behavior_report(text)

print(result)