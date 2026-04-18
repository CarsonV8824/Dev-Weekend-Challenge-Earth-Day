from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QStackedWidget, QPushButton, QLabel, QLineEdit
)

from PySide6.QtCore import Qt

import sys
import os

class Home(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel(self.get_home_text())
        label.setAlignment(Qt.AlignCenter & Qt.AlignTop)
        layout.addWidget(label)

        name_entry = QLineEdit()
        layout.addWidget(name_entry)

    def get_home_text(self):
        path = os.path.join("menus", "html", "home.html")
        with open(path) as f:
            data = f.read()
        return data