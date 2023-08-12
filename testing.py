from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QRadioButton,
    QGroupBox,
    QButtonGroup,
)

from window import Window

testing_window = Window('Тестування')

back_to_topic_button = QPushButton('Назад')
back_to_topic_button.setObjectName('back_to_topic_button')

# Menu
testing_menu_button = QPushButton('Меню')
testing_menu_button.setObjectName('testing_menu_button')

header_testing_button_layout = QHBoxLayout()
header_testing_button_layout.addWidget(back_to_topic_button, alignment=Qt.AlignmentFlag.AlignLeft)
header_testing_button_layout.addSpacing(1)
header_testing_button_layout.addWidget(testing_menu_button, alignment=Qt.AlignmentFlag.AlignRight)

# Питання QLabel
testing_question_label = QLabel('Питання...')
testing_question_label.setObjectName('testing_question_label')
testing_question_label_layout = QHBoxLayout()
testing_question_label_layout.addWidget(testing_question_label,
                                        alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

# Radio buttons
radio_group_box = QGroupBox("Варіанти відповідей:")
radio_group_box.setObjectName('radio_group_box')
radio_group = QButtonGroup()

radio_btn_1 = QRadioButton('1')
radio_btn_2 = QRadioButton('2')
radio_btn_3 = QRadioButton('3')
radio_btn_4 = QRadioButton('4')

radio_group.addButton(radio_btn_1)
radio_group.addButton(radio_btn_2)
radio_group.addButton(radio_btn_3)
radio_group.addButton(radio_btn_4)

radio_buttons_top_layout = QHBoxLayout()
radio_buttons_top_layout.addWidget(radio_btn_1)
radio_buttons_top_layout.addWidget(radio_btn_3)

radio_buttons_bottom_layout = QHBoxLayout()
radio_buttons_bottom_layout.addWidget(radio_btn_2)
radio_buttons_bottom_layout.addWidget(radio_btn_4)

radio_buttons_layout = QVBoxLayout()
radio_buttons_layout.addLayout(radio_buttons_top_layout)
radio_buttons_layout.addLayout(radio_buttons_bottom_layout)

radio_group_box.setLayout(radio_buttons_layout)

testing_questions_layout = QVBoxLayout()

testing_questions_layout.addWidget(radio_group_box, stretch=1)

# answer buttons
testing_answer_button = QPushButton('Відповісти')
testing_answer_button.setObjectName('testing_answer_button')
testing_answer_button_layout = QHBoxLayout()
testing_answer_button_layout.addWidget(testing_answer_button)

testing_layout = QVBoxLayout()
testing_layout.addLayout(header_testing_button_layout)
testing_layout.addLayout(testing_question_label_layout)
testing_layout.addLayout(testing_questions_layout)
testing_layout.addLayout(testing_answer_button_layout)

testing_window.setLayout(testing_layout)


def reset_select_question():
    radio_group.setExclusive(False)
    radio_group.setExclusive(True)
    radio_group.setExclusive(False)
    radio_btn_1.setChecked(False)
    radio_btn_2.setChecked(False)
    radio_btn_3.setChecked(False)
    radio_btn_4.setChecked(False)
    radio_group.setExclusive(True)
