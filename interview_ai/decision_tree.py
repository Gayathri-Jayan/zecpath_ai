from interview_ai.followup_engine import generate_followup


class InterviewDecisionTree:

    def __init__(self):

        self.history = []

    def evaluate(

            self,

            question,

            answer):

        result = generate_followup(

            question,

            answer
        )

        self.history.append(

            {

                "question":

                    question,

                "answer":

                    answer,

                "decision":

                    result["trigger"]
            }
        )

        return result