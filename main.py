from application import app
from greeting import window_greeting, continue_button
from topic import window_topic

window_greeting.show()


def click_continue_button():
    window_greeting.hide()
    window_topic.show()


continue_button.clicked.connect(click_continue_button)

app.exec()
