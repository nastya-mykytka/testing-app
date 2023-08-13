from random import shuffle

from admin import AdminWindow
from application import app
from data import Form, FormView, AnswerCheck
from greeting import window_greeting, continue_button
from questions_data import question_python_data, question_math_data, question_geography_data, question_english_data
from testing import (
    testing_window,
    back_to_topic_button,
    testing_menu_button,
    testing_question_label,
    radio_btn_1,
    radio_btn_2,
    radio_btn_3,
    radio_btn_4,
    reset_select_question,
    testing_answer_button
)
from topic import window_topic, python_button, math_button, geography_button, english_button
from dialog_test_result import TestResulDialog

window_greeting.show()

data_list = []

current_question_index = 0

form = Form()
form_view = FormView(form, testing_question_label, radio_btn_1, radio_btn_2, radio_btn_3, radio_btn_4)
form_answer_check = AnswerCheck(form_view, testing_question_label, radio_btn_1, radio_btn_2, radio_btn_3, radio_btn_4)
admin_window = AdminWindow(data_list, testing_window)
test_result_dialog = TestResulDialog(None, form.correct, form.wrong)

def load_questions(topic_key):
    global data_list
    if topic_key == 'python':
        data_list = question_python_data
    elif topic_key == 'math':
        data_list = question_math_data
    elif topic_key == 'english':
        data_list = question_english_data
    elif topic_key == 'geography':
        data_list = question_geography_data


def set_form_instance():
    index = form.current_question_index
    questions_list = [
        data_list[index]['right'],
        data_list[index]['wrong'][0],
        data_list[index]['wrong'][1],
        data_list[index]['wrong'][2]
    ]
    # shuffle(questions_list)
    # потрібно перемішувати разом з віджетами
    form.set_form_data(
        data_list[index]['question'],
        questions_list[0],
        questions_list[1],
        questions_list[2],
        questions_list[3],
    )


def click_continue_button():
    window_greeting.hide()
    window_topic.show()


def click_python_button():
    load_questions('python')
    set_form_instance()
    form_view.set_form_model(form)
    form_view.show()
    window_topic.hide()
    testing_window.show()


def click_math_button():
    load_questions('math')
    set_form_instance()
    form_view.set_form_model(form)
    form_view.show()
    window_topic.hide()
    testing_window.show()


def click_english_button():
    load_questions('english')
    set_form_instance()
    form_view.set_form_model(form)
    form_view.show()
    window_topic.hide()
    testing_window.show()


def click_geography_button():
    load_questions('geography')
    set_form_instance()
    form_view.set_form_model(form)
    form_view.show()
    window_topic.hide()
    testing_window.show()


def reset_test():
    testing_answer_button.setText('Відповісти')
    form.current_question_index = 0
    form.correct = 0
    form.wrong = 0
    reset_select_question()


def click_back_python_button():
    reset_test()
    testing_window.hide()
    window_topic.show()


def click_menu_python_button():
    reset_select_question()
    testing_window.hide()
    admin_window.update_data_list(data_list)
    admin_window.show()


def test_result_dialog_closed():
    testing_window.hide()
    reset_test()
    window_greeting.show()


def show_test_result():
    test_result_dialog.calculate_result(form.correct, len(data_list))
    test_result_dialog.dialog_closed.connect(test_result_dialog_closed)  # Connect the signal to the function
    test_result_dialog.exec()


def start_test():
    reset_test()
    admin_window.hide()
    set_form_instance()
    form_view.set_form_model(form)
    form_view.show()
    testing_window.show()


def click_testing_answer_button():
    if radio_btn_1.isChecked() or radio_btn_2.isChecked() or radio_btn_3.isChecked() or radio_btn_4.isChecked():
        if form.current_question_index == len(data_list) - 1:
            form_answer_check.set_form_model(form)
            form_answer_check.check()
            show_test_result()
            return

        form_answer_check.set_form_model(form)
        form_answer_check.check()
        reset_select_question()
        set_form_instance()
        form_view.set_form_model(form)
        form_view.show()

        if form.current_question_index + 1 == len(data_list):
            testing_answer_button.setText('Результат теста')


continue_button.clicked.connect(click_continue_button)
python_button.clicked.connect(click_python_button)
math_button.clicked.connect(click_math_button)
english_button.clicked.connect(click_english_button)
geography_button.clicked.connect(click_geography_button)

back_to_topic_button.clicked.connect(click_back_python_button)
testing_menu_button.clicked.connect(click_menu_python_button)
testing_answer_button.clicked.connect(click_testing_answer_button)

admin_window.start_test_button.clicked.connect(start_test)

test_result_dialog.dialog_closed.connect(test_result_dialog_closed)

app.exec()
