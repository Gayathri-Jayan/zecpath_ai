import json

from interview_ai.interview_simulator import simulate_multiple

with open(
    "interview_ai/candidate_profiles.json",
    "r"
) as file:

    candidates = json.load(file)

results = simulate_multiple(candidates)

print(results)