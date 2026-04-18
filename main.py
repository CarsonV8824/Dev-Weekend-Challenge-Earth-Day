from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QStackedWidget, QPushButton, QLabel
)
import pygame
import sys
from menus.main_window import MainWindow

from data.state import state
from data.database import Database


def main():
    def_state = Database.get_data_by_name("Player1")
    app = QApplication(sys.argv)
    window = MainWindow(def_state)
    window.resize(400, 300)
    window.show()
    app.exec()
    Database.insert_data(window.game_state)
    sys.exit()

if __name__ == "__main__":
    main()