import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns

import pandas as pd

from data.database import Database

"""Example:
class GraphWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create figure and canvas
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        
        # Create layout and add canvas
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
        # Plot with seaborn
        ax = self.figure.add_subplot(111)
        sns.scatterplot(x='col1', y='col2', data=df, ax=ax)
        self.canvas.draw()
        
    def get_graph(self):
        new_data:pd.DataFrame | None = getStockData(self.stock_name.text())
        if type(new_data) == None:
            print(new_data)
            QMessageBox.warning(
                self, 
                "Error",
                "Error Getting Stock data. Check inputs"
            )
        self.ax.clear()
        df = new_data.reset_index()
        sns.lineplot(data=df, x="Date", y="Close", ax=self.ax).set_title(f"Stock of {self.stock_name.text()}")
        self.canvas.draw()
        """

class Stats(QWidget):
    def __init__(self):
        super().__init__()

        self.figure = Figure(figsize=(10, 8), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.ax1 = self.figure.add_subplot(221)
        self.ax2 = self.figure.add_subplot(222)
        self.ax3 = self.figure.add_subplot(223)

        self.refresh_charts()

    def refresh_charts(self):
        """Refresh all chart data and redraw."""
        self.ax1.clear()
        self.score_data = Database.get_top_10_score()
        sns.barplot(data=self.score_data, x="names", y="scores", ax=self.ax1)
        self.ax1.set_title("Top 10 Scores")
        self.ax1.tick_params(axis='x', rotation=45)

        self.ax2.clear()
        self.alantic_wins = Database.get_top_10_atlantic_wins()
        sns.barplot(data=self.alantic_wins, x="names", y="atlantic wins", ax=self.ax2)
        self.ax2.set_title("Top 10 Atlantic Wins")
        self.ax2.tick_params(axis='x', rotation=45)

        self.ax3.clear()
        self.pacific_data = Database.get_top_10_pacific_wins()
        sns.barplot(data=self.pacific_data, x="names", y="pacific wins", ax=self.ax3)
        self.ax3.set_title("Top 10 Pacific Wins")
        self.ax3.tick_params(axis='x', rotation=45)

        self.figure.tight_layout()
        self.canvas.draw()

    def update(self):
        self.refresh_charts()



