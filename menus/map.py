from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QStackedWidget, QPushButton, QLabel
)
from PySide6.QtCore import Signal
import sys

class Map(QWidget):
    atlantic_map = Signal()
    pacific_map = Signal()
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        atlantic_btn = QPushButton("Atlantic")
        atlantic_btn.clicked.connect(self.atlantic_map.emit)
        layout.addWidget(atlantic_btn)

        pacific_btn = QPushButton("Pacific")
        pacific_btn.clicked.connect(self.pacific_map.emit)
        layout.addWidget(pacific_btn)