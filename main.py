from random import shuffle

from admin import AdminWindow
from application import app
from data import Form, FormView
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

window_greeting.show()

data_list = []

current_question_index = 0

form = Form()
form_view = None


def create_form_view():
    global form_view
    form_view = FormView(
        form,
        testing_question_label,
        radio_btn_1,
        radio_btn_2,
        radio_btn_3,
        radio_btn_4,
    )


create_form_view()

admin_window = AdminWindow(data_list, testing_window)


def load_questions(topic):
    global data_list
    if topic == 'python':
        data_list = question_python_data
    elif topic == 'math':
        data_list = question_math_data
    elif topic == 'english':
        data_list = question_english_data
    elif topic == 'geography':
        data_list = question_geography_data


def create_form_instance(index=0):
    global form
    questions_list = [
        data_list[index]['right'],
        data_list[index]['wrong'][0],
        data_list[index]['wrong'][1],
        data_list[index]['wrong'][2]
    ]
    shuffle(questions_list)
    form = Form(
        data_list[index]['question'],
        questions_list[0],
        questions_list[1],
        questions_list[2],
        questions_list[3],
    )
    return form


def click_continue_button():
    window_greeting.hide()
    window_topic.show()
    form_view.show()


def update_admin_content_list():
    admin_window.update_content_list(data_list)


def click_python_button():
    global data_list
    load_questions('python')
    create_form_instance()
    form_view.change(form)
    form_view.show()
    window_topic.hide()
    testing_window.show()
    admin_window.update_content_list(data_list)


def click_math_button():
    global data_list
    load_questions('math')
    create_form_instance()
    form_view.change(form)
    form_view.show()
    window_topic.hide()
    testing_window.show()


def click_english_button():
    global data_list
    load_questions('english')
    create_form_instance()
    form_view.change(form)
    form_view.show()
    window_topic.hide()
    testing_window.show()


def click_geography_button():
    global data_list
    load_questions('geography')
    create_form_instance()
    form_view.change(form)
    form_view.show()
    window_topic.hide()
    testing_window.show()


def click_back_python_button():
    reset_select_question()
    testing_window.hide()
    window_topic.show()


def click_menu_python_button():
    reset_select_question()
    testing_window.hide()
    admin_window.update_data_list(data_list)
    admin_window.show()


def click_start_test():
    reset_select_question()
    admin_window.hide()
    testing_window.show()


def show_test_result():
    print('Show result')


def click_testing_answer_button():
    global current_question_index
    if current_question_index + 1 < len(data_list):
        current_question_index += 1
        create_form_instance(current_question_index)
        form_view.change(form)
        testing_answer_button.setText('Відповісти')
    else:
        testing_answer_button.setText('Результат теста')
        show_test_result()


continue_button.clicked.connect(click_continue_button)
python_button.clicked.connect(click_python_button)
math_button.clicked.connect(click_math_button)
english_button.clicked.connect(click_english_button)
geography_button.clicked.connect(click_geography_button)

back_to_topic_button.clicked.connect(click_back_python_button)
testing_menu_button.clicked.connect(click_menu_python_button)
testing_answer_button.clicked.connect(click_testing_answer_button)

app.exec()

