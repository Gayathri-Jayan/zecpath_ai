INTERVIEW_FLOW = {

    "Introduction": [

        "Welcome",

        "Verify Candidate",

        "Self Introduction"
    ],

    "Core HR Questions": [

        "Career Journey",

        "Strengths",

        "Weaknesses",

        "Teamwork",

        "Career Goals"
    ],

    "Role-Based Evaluation": [

        "Role Specific Questions",

        "Experience Validation"
    ],

    "Closing": [

        "Availability",

        "Questions From Candidate",

        "End Interview"
    ]
}


if __name__ == "__main__":

    for phase, steps in INTERVIEW_FLOW.items():

        print()

        print(phase)

        for step in steps:

            print(" -", step)