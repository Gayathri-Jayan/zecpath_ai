from screening_ai.robust_flow import process_candidate_response

cases = [

    "",

    "[noise] I have 3 years experience",

    "[poor_audio]",

    "[mixed] ഞാൻ Python developer ആണ്",

    "I have 3 years experience in Python"
]

for case in cases:

    print(process_candidate_response(case))