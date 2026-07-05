# -----------------------------------
# AI Screening Report Generator
# -----------------------------------

def generate_screening_report(candidate, answers):

    strengths = []
    risks = []
    missing = []

    confirmed_skills = []

    salary = "Not Mentioned"
    availability = "Unknown"

    key_answers = []

    for answer in answers:

        key_answers.append({

            "question_id": answer["question_id"],

            "answer": answer["original_text"]

        })

        confirmed_skills.extend(

            answer.get("skills", [])
        )

        if answer.get("salary"):

            salary = answer["salary"]

        if answer.get("availability") != "Unknown":

            availability = answer["availability"]

        if answer.get("overall", 0) >= 80:

            strengths.append(

                f"Strong response for {answer['question_id']}"
            )

        elif answer.get("overall", 0) < 60:

            risks.append(

                f"Weak response for {answer['question_id']}"
            )

        if answer.get("is_vague"):

            missing.append(

                f"Vague answer in {answer['question_id']}"
            )

    confirmed_skills = list(

        set(confirmed_skills)
    )

    return {

        "candidate_id":

            candidate["candidate_id"],

        "job_id":

            candidate["job_id"],

        "key_answers":

            key_answers,

        "strengths":

            strengths,

        "risks":

            risks,

        "missing_data":

            missing,

        "salary_expectation":

            salary,

        "availability":

            availability,

        "confirmed_skills":

            confirmed_skills
    }

def export_report(report):

    print("=" * 50)

    print("AI SCREENING REPORT")

    print("=" * 50)

    print("Candidate :", report["candidate_id"])

    print("Job :", report["job_id"])

    print()

    print("Strengths")

    for item in report["strengths"]:

        print("-", item)

    print()

    print("Risks")

    for item in report["risks"]:

        print("-", item)

    print()

    print("Missing Data")

    for item in report["missing_data"]:

        print("-", item)

    print()

    print("Salary :", report["salary_expectation"])

    print("Availability :", report["availability"])

    print("Skills :", ", ".join(report["confirmed_skills"]))


def export_report_text(report):

    text = f"""
=========================================
AI SCREENING REPORT
=========================================

Candidate ID : {report['candidate_id']}
Job ID       : {report['job_id']}

Final Score  : {report['final_score']}
Decision     : {report['decision']}

----- Strengths -----
{chr(10).join(report['summary']['strengths'])}

----- Risks -----
{chr(10).join(report['summary']['risks'])}

----- Missing Data -----
{chr(10).join(report['summary']['missing_data'])}

----- Highlights -----
Salary       : {report['highlights']['salary_expectation']}
Availability : {report['highlights']['availability']}
Skills       : {', '.join(report['highlights']['confirmed_skills'])}
"""

    return text