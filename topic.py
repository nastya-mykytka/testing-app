from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
)
from window import Window

window_topic = Window('Вибір теми')

topik_label = QLabel('Виберіть тему для тестування')
topik_label.setObjectName('topik_label')
topik_label_layout = QHBoxLayout()
topik_label_layout.addWidget(topik_label, alignment=Qt.AlignmentFlag.AlignCenter)

python_button = QPushButton("Python")
python_button.setObjectName('python_button')

math_button = QPushButton("Математика")
math_button.setObjectName('math_button')

english_button = QPushButton("Англійська")
english_button.setObjectName('english_button')

geography_button = QPushButton("Географія")
geography_button.setObjectName('geography_button')

top_layout = QHBoxLayout()
top_layout.addWidget(python_button)
top_layout.addWidget(math_button)

bott_layout = QHBoxLayout()
bott_layout.addWidget(english_button)
bott_layout.addWidget(geography_button)

topic_layout = QVBoxLayout()
topic_layout.addLayout(topik_label_layout)
topic_layout.addLayout(top_layout)
topic_layout.addLayout(bott_layout)

window_topic.setLayout(topic_layout)

