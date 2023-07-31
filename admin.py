from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QDialog,
)

from dialog_form import AddQuestionDialog
from window import Window


class AdminWindow(Window):
    def __init__(self, data_list, testing_window):
        super().__init__('Admin')
        self.data_list = data_list
        self.testing_window = testing_window

        self.content_layout = QVBoxLayout()

        start_test_button = QPushButton('Почати тест')
        start_test_button.setObjectName('start_test_button')

        add_test_button = QPushButton('Додати питання')
        add_test_button.setObjectName('add_test_button')

        footer_button_layout = QHBoxLayout()
        footer_button_layout.addWidget(start_test_button,
                                       alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
        footer_button_layout.addWidget(add_test_button,
                                       alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)

        main_admin_layout = QVBoxLayout()
        main_admin_layout.addLayout(self.content_layout, stretch=1)
        main_admin_layout.addLayout(footer_button_layout)

        self.setLayout(main_admin_layout)

        add_test_button.clicked.connect(self.show_add_question_dialog)
        start_test_button.clicked.connect(self.start_test)

    def remove_layout(self, layout):
        # Deleting the layout and its widgets to free up memory
        for i in reversed(range(layout.count())):
            item = layout.takeAt(i)
            if item.layout():
                self.remove_layout(item.layout())
            elif item.widget():
                item.widget().deleteLater()

    def update_data_list(self, data_list):
        self.data_list = data_list
        self.update_content_list(self.data_list)

    def remove_question(self, data_list, question_data):
        data_list.remove(question_data)
        self.update_content_list(data_list)

    def update_content_list(self, data_list=[]):
        self.remove_layout(self.content_layout)

        # Create QLabel, Edit Button, and Remove Button for each question
        for index, question_data in enumerate(data_list):
            question_item = QLabel(question_data["question"])
            question_item.setObjectName('question_item')

            edit_button = QPushButton('Редагувати')
            edit_button.setObjectName('edit_button')
            edit_button.clicked.connect(lambda _, data=question_data, i=index: self.show_edit_question_dialog(data, i))

            remove_button = QPushButton('Видалити')
            remove_button.setObjectName('remove_button')
            remove_button.clicked.connect(lambda _, data=question_data: self.remove_question(data_list, data))

            item_layout = QHBoxLayout()
            item_layout.addWidget(question_item, stretch=1)
            item_layout.addWidget(edit_button)
            item_layout.addWidget(remove_button)

            self.content_layout.addLayout(item_layout)

    def show_add_question_dialog(self):
        dialog = AddQuestionDialog(self)
        dialog.questionAdded.connect(lambda new_question: self.handle_new_question(new_question))
        if dialog.exec_() == QDialog.Accepted:
            pass

    def start_test(self):
        self.hide()
        self.testing_window.show()

    def show_edit_question_dialog(self, data, index):
        dialog = AddQuestionDialog(
            self,
            data["question"],
            data["right"],
            data["wrong"][0],
            data["wrong"][1],
            data["wrong"][2],
        )
        dialog.questionAdded.connect(lambda new_question: self.handle_edit_question(new_question, index))
        if dialog.exec_() == QDialog.Accepted:
            pass

    def handle_new_question(self, new_question):
        self.data_list.append(new_question)
        self.update_content_list(self.data_list)

    def handle_edit_question(self, new_question, index):
        self.data_list[index] = new_question
        self.update_content_list(self.data_list)
