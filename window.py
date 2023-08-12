from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDesktopWidget


class Window(QWidget):
    def __init__(self, title='Window', size_x=1200, size_y=800):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(size_x, size_y)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
