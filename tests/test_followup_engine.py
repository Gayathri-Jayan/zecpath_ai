from interview_ai.decision_tree import InterviewDecisionTree

tree = InterviewDecisionTree()

result = tree.evaluate(

    "Tell me about yourself.",

    "I am confident and developed many Python projects."
)

print(result)