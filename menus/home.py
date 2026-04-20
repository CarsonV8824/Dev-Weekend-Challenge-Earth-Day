from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QLabel, QLineEdit
)

from PySide6.QtCore import Qt, Signal

import sys
import os

from data.database import Database
from data.state import state

# Get project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Home(QWidget):
    name_submitted = Signal(str)  # Signal to emit when name is saved
    
    def __init__(self):
        super().__init__()
        
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        label = QLabel(self.get_home_text())
        label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(label)

        # Create a centered container for name entry and button
        input_layout = QVBoxLayout()
        input_layout.setContentsMargins(0, 0, 0, 0)
        
        self.name_entry = QLineEdit()
        self.name_entry.setMaximumWidth(400)
        input_layout.addWidget(self.name_entry, alignment=Qt.AlignCenter)

        submit = QPushButton("Enter Name")
        submit.setMaximumWidth(400)
        submit.clicked.connect(self.save_name_as_user)
        input_layout.addWidget(submit, alignment=Qt.AlignCenter)

        # Add input layout to main layout
        main_layout.addLayout(input_layout)
        main_layout.addStretch()

    def get_home_text(self):
        path = os.path.join(PROJECT_ROOT, "menus", "html", "home.html")
        with open(path) as f:
            data = f.read()
        return data
    
    def save_name_as_user(self):
        name = self.name_entry.text()
        self.name_submitted.emit(name)  # Emit the signal