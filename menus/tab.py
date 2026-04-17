from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QStackedWidget, QPushButton, QLabel, QHBoxLayout
)
from PySide6.QtCore import Signal
import sys

class Tab(QWidget):
    home_page = Signal()
    map_page = Signal()
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        home = QPushButton("Home")
        home.clicked.connect(self.home_page.emit)
        layout.addWidget(home)

        map_page_btn = QPushButton("Map")
        map_page_btn.clicked.connect(self.map_page.emit)
        layout.addWidget(map_page_btn)