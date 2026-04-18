from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QStackedWidget, QPushButton, QLabel
)
import sys
import threading

from menus.tab import Tab
from menus.home import Home
from menus.map import Map

from oceans.alantic import alantic

class MainWindow(QMainWindow):
    def __init__(self, game_state):
        self.game_state = game_state
        self.home_page = None
        self.stack = None
        self.game_thread = None

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

        self.home_page = Home()
        self.stack.addWidget(self.home_page)

        map_page = Map()
        self.stack.addWidget(map_page)
        map_page.alantic_map.connect(self.play_alantic)

        tab.home_page.connect(lambda: self.stack.setCurrentWidget(self.home_page))
        tab.map_page.connect(lambda: self.stack.setCurrentWidget(map_page))        

        layout.addWidget(self.stack)
        self.setCentralWidget(container)

    def play_alantic(self):
        # Wait for previous game to finish
        if self.game_thread and self.game_thread.is_alive():
            self.game_thread.join()
        
        self.game_thread = threading.Thread(target=alantic, args=(self.game_state,), daemon=False)
        self.game_thread.start()
