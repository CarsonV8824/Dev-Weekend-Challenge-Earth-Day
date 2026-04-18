from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QStackedWidget, QPushButton, QLabel
)
import sys
import os

class Home(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel(self.get_home_text())
        layout.addWidget(label)

    def get_home_text(self):
        path = os.path.join("menus", "html", "home.html")
        with open(path) as f:
            data = f.read()
        return data