from application import app
from greeting import window_greeting, continue_button
from topic import window_topic, python_button, math_button, geography_button, english_button
from python import python_window
from mathematics import math_window
from english import english_window
from geography import geography_window

window_greeting.show()


def click_continue_button():
    window_greeting.hide()
    window_topic.show()


def click_python_button():
    window_topic.hide()
    python_window.show()


def click_math_button():
    window_topic.hide()
    math_window.show()

def click_english_button():
    window_topic.hide()
    english_window.show()

def click_geography_button():
        window_topic.hide()
        geography_window.show()




continue_button.clicked.connect(click_continue_button)
python_button.clicked.connect(click_python_button)
math_button.clicked.connect(click_math_button)
english_button.clicked.connect(click_english_button)
geography_button.clicked.connect(click_geography_button)

app.exec()
