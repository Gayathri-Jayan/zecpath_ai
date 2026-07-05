from interview_ai.hr_interview_engine import HRInterviewEngine

engine = HRInterviewEngine(

    "Fresher",

    "Technical"
)

print(engine.interview_categories())

print()

for question in engine.generate_questions():

    print(question)