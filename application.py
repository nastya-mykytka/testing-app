from pathlib import Path

from PyQt5.QtWidgets import QApplication

app = QApplication([])
app.setStyleSheet(Path('app.css').read_text())
