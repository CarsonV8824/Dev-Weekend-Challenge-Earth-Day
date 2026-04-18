from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QStackedWidget, QPushButton, QLabel
)
import pygame
import sys
import os
from menus.main_window import MainWindow

from data.database import Database

def get_style_file_stuff():
    with open(os.path.join("assets", "styles.css"), encoding='utf-8') as f:
        data = f.read()
    return data

def main():
    def_state = Database.get_data_by_name("Player1")
    app = QApplication(sys.argv)
    app.setStyleSheet(get_style_file_stuff())
    window = MainWindow(def_state)
    window.resize(400, 300)
    window.show()
    app.exec()
    Database.insert_data(window.game_state)
    sys.exit()

if __name__ == "__main__":
    main()