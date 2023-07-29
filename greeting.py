from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
)
from window import Window


window_greeting = Window('Привітання')

greeting_title = QLabel('Вітаю тебе на моїй платформі для тестування!')
greeting_title.setObjectName('greeting_title')
greeting_sub_title = QLabel('Щоб почати тестування нажми кнопку Продовжити')
greeting_sub_title.setObjectName('greeting_sub_title')

continue_button = QPushButton('Продовжити')
continue_button.setObjectName('continue_button')
greeting_layout = QVBoxLayout()
greeting_layout.addWidget(greeting_title, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom, stretch=2)
greeting_layout.addWidget(greeting_sub_title, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop, stretch=2)
greeting_layout.addWidget(continue_button, alignment=Qt.AlignmentFlag.AlignCenter, stretch=1)
window_greeting.setLayout(greeting_layout)











