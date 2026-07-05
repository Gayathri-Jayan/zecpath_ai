class ConversationStateMachine:

    def __init__(self):

        self.state = "START"

    def transition(self, event):

        if self.state == "START":

            self.state = "ASK_QUESTION"

        elif self.state == "ASK_QUESTION":

            if event == "followup":

                self.state = "FOLLOW_UP"

            elif event == "next":

                self.state = "ASK_QUESTION"

            elif event == "finish":

                self.state = "END"

        elif self.state == "FOLLOW_UP":

            self.state = "ASK_QUESTION"

        return self.state