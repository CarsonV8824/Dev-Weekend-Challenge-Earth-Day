from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QStackedWidget, QPushButton, QLabel
)
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QIcon
import sys
import threading
import os

from menus.tab import Tab
from menus.home import Home
from menus.map import Map
from menus.stats import Stats

from oceans.atlantic import atlantic
from oceans.pacific import pacific

from data.database import Database
from data.state import state

class GameThreadSignals(QObject):
    """Signals for game thread completion."""
    game_finished = Signal()

class MainWindow(QMainWindow):
    def __init__(self, game_state:dict):
        self.game_state:dict = game_state
        self.home_page = None
        self.stack = None
        self.game_thread = None
        self.stats_page = None
        self.game_signals = GameThreadSignals()

        super().__init__()

        self.setWindowTitle("Franklin and the Diver")
        # Set window icon
        icon_path = os.path.join("assets", "Net.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

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
        map_page.atlantic_map.connect(self.play_atlantic)
        map_page.pacific_map.connect(self.play_pacific)

        self.stats_page = Stats()
        self.stack.addWidget(self.stats_page)
        
        # Connect game completion signal to stats refresh
        self.game_signals.game_finished.connect(self.stats_page.refresh_charts)

        tab.home_page.connect(lambda: self.stack.setCurrentWidget(self.home_page))
        tab.map_page.connect(lambda: self.stack.setCurrentWidget(map_page))   
        tab.stats_page.connect(lambda: (self.stack.setCurrentWidget(self.stats_page), self.stats_page.update()))

        
        layout.addWidget(self.stack)
        self.setCentralWidget(container)

    def play_atlantic(self):
        # Wait for previous game to finish
        if self.game_thread and self.game_thread.is_alive():
            self.game_thread.join()
        
        self.game_thread = threading.Thread(target=self._atlantic_game_thread, daemon=False)
        self.game_thread.start()

    def play_pacific(self):
        # Wait for previous game to finish
        if self.game_thread and self.game_thread.is_alive():
            self.game_thread.join()
        
        self.game_thread = threading.Thread(target=self._pacific_game_thread, daemon=False)
        self.game_thread.start()

    def _atlantic_game_thread(self):
        """Run atlantic game and refresh stats when complete."""
        atlantic(self.game_state)
        # Emit signal to refresh stats on main thread
        self.game_signals.game_finished.emit()

    def _pacific_game_thread(self):
        """Run pacific game and refresh stats when complete."""
        pacific(self.game_state)
        # Emit signal to refresh stats on main thread
        self.game_signals.game_finished.emit()
    
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