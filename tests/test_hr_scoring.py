from interview_ai.hr_score_report import generate_hr_report

report = generate_hr_report(

    "C101",

    "I have worked on Python and Django projects for two years.",

    90
)

print(report)

assert report["score_breakdown"]["final_hr_score"] > 0