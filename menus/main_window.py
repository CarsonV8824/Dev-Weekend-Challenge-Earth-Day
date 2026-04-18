from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QStackedWidget, QPushButton, QLabel
)
import sys
import threading

from menus.tab import Tab
from menus.home import Home
from menus.map import Map
from menus.stats import Stats

from oceans.alantic import alantic
from oceans.pacific import pacific

from data.database import Database
from data.state import state

class MainWindow(QMainWindow):
    def __init__(self, game_state:dict):
        self.game_state:dict = game_state
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
        self.home_page.name_submitted.connect(self.update_game_state)
        self.stack.addWidget(self.home_page)

        map_page = Map()
        self.stack.addWidget(map_page)
        map_page.alantic_map.connect(self.play_alantic)
        map_page.pacific_map.connect(self.play_pacific)

        stats_page = Stats()
        self.stack.addWidget(stats_page)  

        tab.home_page.connect(lambda: self.stack.setCurrentWidget(self.home_page))
        tab.map_page.connect(lambda: self.stack.setCurrentWidget(map_page))   
        tab.stats_page.connect(lambda: (self.stack.setCurrentWidget(stats_page), stats_page.update()))

        
        layout.addWidget(self.stack)
        self.setCentralWidget(container)

    def play_alantic(self):
        # Wait for previous game to finish
        if self.game_thread and self.game_thread.is_alive():
            self.game_thread.join()
        
        self.game_thread = threading.Thread(target=alantic, args=(self.game_state,), daemon=False)
        self.game_thread.start()

    def play_pacific(self):
        # Wait for previous game to finish
        if self.game_thread and self.game_thread.is_alive():
            self.game_thread.join()
        
        self.game_thread = threading.Thread(target=pacific, args=(self.game_state,), daemon=False)
        self.game_thread.start()
    
    def update_game_state(self, name: str):
        """Update game_state with player data when name is submitted."""
        
        
        existing_data = Database.get_data_by_name(name)
        if existing_data and existing_data["name"] == name:
            # Player exists, use existing data
            self.game_state.update(existing_data)
        else:
            # New player, create and save to database
            new_data = state(name)
            self.game_state.update(new_data)
            Database.insert_data(new_data)