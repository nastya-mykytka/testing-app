from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QLineEdit, QFormLayout, QPushButton, QTextEdit


class AddQuestionDialog(QDialog):
    questionAdded = pyqtSignal(dict)

    def __init__(self, parent=None, question='', answer='', wrong_1='', wrong_2='', wrong_3=''):
        super(AddQuestionDialog, self).__init__(parent)


        self.setWindowTitle('Додати питання')
        self.txt_question = QTextEdit(question)
        self.txt_answer = QLineEdit(answer)
        self.txt_wrong_1 = QLineEdit(wrong_1)
        self.txt_wrong_2 = QLineEdit(wrong_2)
        self.txt_wrong_3 = QLineEdit(wrong_3)

        add_button = QPushButton('Додати')
        add_button.setObjectName('form_add_button')
        add_button.clicked.connect(self.add_question)

        if question or answer or wrong_1 or wrong_2 or wrong_3:
            self.setWindowTitle('Редагувати питання')
            add_button.setText('Редагувати')

        layout_form = QFormLayout()

        layout_form.addRow('Питання:', self.txt_question)
        layout_form.addRow('Правильна відповідь:', self.txt_answer)
        layout_form.addRow('Не правильна відповідь 1:', self.txt_wrong_1)
        layout_form.addRow('Не правильна відповідь 2:', self.txt_wrong_2)
        layout_form.addRow('Не правильна відповідь 3:', self.txt_wrong_3)
        layout_form.addRow(add_button)

        self.setLayout(layout_form)

    def add_question(self):
        question = self.txt_question.toPlainText()
        right = self.txt_answer.text()
        wrong_1 = self.txt_wrong_1.text()
        wrong_2 = self.txt_wrong_2.text()
        wrong_3 = self.txt_wrong_3.text()
        wrong = [wrong_1, wrong_2, wrong_3]

        if question and right and all(wrong):
            new_question = {
                "question": question,
                "right": right,
                "wrong": wrong,
            }
            self.questionAdded.emit(new_question)
            self.accept()
