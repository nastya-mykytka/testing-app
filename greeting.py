from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
)


window_greeting = QWidget()
window_greeting.setWindowTitle('Greeting')
window_greeting.resize(800, 600)

greeting_title = QLabel('Вітаємо тебе на моїй платформі для тестування!')
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











