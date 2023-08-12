class Form():
    def __init__(self, question='', answer='', wrong_answer_1='', wrong_answer_2='', wrong_answer_3=''):
        self.question = question
        self.answer = answer
        self.wrong_answer_1 = wrong_answer_1
        self.wrong_answer_2 = wrong_answer_2
        self.wrong_answer_3 = wrong_answer_3
        self.current_question_index = 0
        self.wrong = 0
        self.correct = 0

    def set_form_data(self, question, answer, wrong_answer_1, wrong_answer_2, wrong_answer_3):
        self.question = question
        self.answer = answer
        self.wrong_answer_1 = wrong_answer_1
        self.wrong_answer_2 = wrong_answer_2
        self.wrong_answer_3 = wrong_answer_3

    def got_right(self):
        self.correct += 1
        self.current_question_index += 1

    def got_wrong(self):
        self.wrong += 1
        self.current_question_index += 1


class FormView():
    def __init__(self, form_model, question, answer, wrong_answer_1, wrong_answer_2, wrong_answer_3):
        self.form_model = form_model
        self.question = question
        self.answer = answer
        self.wrong_answer_1 = wrong_answer_1
        self.wrong_answer_2 = wrong_answer_2
        self.wrong_answer_3 = wrong_answer_3


    def set_form_model(self, form_model):
        self.form_model = form_model

    def show(self):
        self.question.setText(self.form_model.question)
        self.answer.setText(self.form_model.answer)
        self.wrong_answer_1.setText(self.form_model.wrong_answer_1)
        self.wrong_answer_2.setText(self.form_model.wrong_answer_2)
        self.wrong_answer_3.setText(self.form_model.wrong_answer_3)


class AnswerCheck(FormView):
    def __init__(self, form_model, question, answer, wrong_answer_1, wrong_answer_2, wrong_answer_3):
        super().__init__(form_model, question, answer, wrong_answer_1, wrong_answer_2, wrong_answer_3)

    def check(self):
        if self.answer.isChecked():
            self.form_model.got_right()
        else:
            self.form_model.got_wrong()
