from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QStackedWidget, QPushButton, QLabel
)
import pygame
import sys
import os
from menus.main_window import MainWindow

from data.database import Database

# Get project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

def get_style_file_stuff():
    style_path = os.path.join(PROJECT_ROOT, "assets", "styles.css")
    with open(style_path, encoding='utf-8') as f:
        data = f.read()
    return data

def main():
    def_state = Database.get_data_by_name("Player1")
    app = QApplication(sys.argv)
    app.setStyleSheet(get_style_file_stuff())
    window = MainWindow(def_state)
    window.show()
    app.exec()
    Database.insert_data(window.game_state)
    sys.exit()

if __name__ == "__main__":
    main()