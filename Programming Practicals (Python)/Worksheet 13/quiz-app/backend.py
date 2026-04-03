class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class Quiz:

    def __init__(self):
        self.questions = []

    def add_question(self, question, answer):
        new_question = Question(question, answer)
        self.questions.append(new_question)

    def remove_question_at(self, index):
        del self.questions[index]

    def get_question_at(self, index):
        return self.questions[index].question

    def check_answer_at(self, index, user_answer):
        actual_answer = self.questions[index].answer
        if user_answer.get().lower() == actual_answer.lower():
            user_answer.config(bg="green")
            return True
        else:
            user_answer.config(bg="red")
            return False

    def get_num_questions(self):
        return len(self.questions)
