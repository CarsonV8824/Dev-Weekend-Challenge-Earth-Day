from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QStackedWidget, QPushButton, QLabel
)
import sys

from menus.tab import Tab
from menus.home import Home
from menus.map import Map

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stacked Widget Example")

        # --- Central container widget ---
        container = QWidget()
        layout = QVBoxLayout(container)

        # -- tab control

        tab = Tab()
        layout.addWidget(tab)

        # --- Stacked widget ---
        self.stack = QStackedWidget()

        home_page = Home()
        self.stack.addWidget(home_page)

        map_page = Map()
        self.stack.addWidget(map_page)

        tab.home_page.connect(lambda: self.stack.setCurrentWidget(home_page))
        tab.map_page.connect(lambda: self.stack.setCurrentWidget(map_page))        

        layout.addWidget(self.stack)
        self.setCentralWidget(container)
