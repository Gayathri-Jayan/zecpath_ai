class HRInterviewEngine:

    def __init__(

            self,

            candidate_type,

            role_type):

        self.candidate_type = candidate_type

        self.role_type = role_type

    def interview_categories(self):

        return [

            "Self Introduction",

            "Career Journey",

            "Strengths & Weaknesses",

            "Teamwork & Culture Fit",

            "Career Goals",

            "Availability & Commitment"
        ]

    def generate_questions(self):

        if self.candidate_type == "Fresher":

            if self.role_type == "Technical":

                return [

                    "Can you introduce yourself?",

                    "Tell me about your final year project.",

                    "Why should we hire you?"
                ]

            return [

                "Introduce yourself.",

                "What motivates you?",

                "Why do you want this role?"
            ]

        if self.role_type == "Technical":

            return [

                "Tell me about your experience.",

                "Describe your most challenging project.",

                "How do you handle production issues?"
            ]

        return [

            "Describe your leadership experience.",

            "How do you resolve conflicts?",

            "What motivates you?"
        ]