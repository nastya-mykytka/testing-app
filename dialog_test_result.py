from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QDialog, QLabel, QHBoxLayout, QVBoxLayout


class TestResulDialog(QDialog):
    test_result = pyqtSignal(dict)
    dialog_closed = pyqtSignal()

    def __init__(self, parent=None, correct_count=0, wrong_count=0, time=0):
        super(TestResulDialog, self).__init__(parent)

        self.setWindowTitle('Результат теста')
        self.resize(600, 300)

        self.title = QLabel()
        title_layout = QHBoxLayout()
        title_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)

        self.result = QLabel()
        self.result_label = QLabel('Результат теста у %')
        result_layout = QHBoxLayout()
        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.result)

        self.correct_count = QLabel(str(correct_count))
        self.correct_count_label = QLabel('Кількість правильних відповідей')
        correct_count_layout = QHBoxLayout()
        correct_count_layout.addWidget(self.correct_count_label)
        correct_count_layout.addWidget(self.correct_count)

        self.wrong_count = QLabel(str(wrong_count))
        self.wrong_count_label = QLabel('Кількість не правильних відповідей')
        wrong_count_layout = QHBoxLayout()
        wrong_count_layout.addWidget(self.wrong_count_label)
        wrong_count_layout.addWidget(self.wrong_count)

        self.time_label = QLabel('Час проходження таста')
        self.time = QLabel(str(time))
        time_layout = QHBoxLayout()
        time_layout.addWidget(self.time_label)
        time_layout.addWidget(self.time)

        layout = QVBoxLayout()
        layout.addLayout(title_layout)
        layout.addLayout(result_layout)
        layout.addLayout(correct_count_layout)
        layout.addLayout(wrong_count_layout)
        layout.addLayout(time_layout)

        self.setLayout(layout)

    def calculate_result(self, correct_count, question_count):
        # correct_count = int(self.correct_count.text())
        print(correct_count)

        result = (correct_count / question_count) * 100
        self.result.setText('{}%'.format(result))
        if result > 60:
            self.title.setText('Вітаю! Ти пройшов тест')
        else:
            self.title.setText('На жаль ти не пройшов тест')  # Fixed typo in label text

    def closeEvent(self, event):
        self.dialog_closed.emit()  # Emit the dialog_closed signal when the dialog is closed
        super(TestResulDialog, self).closeEvent(event)

