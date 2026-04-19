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
        self.figure.patch.set_facecolor('#02253A')  # Deep ocean blue from styles.css
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
        # Color scheme from styles.css
        dark_ocean = '#02253A'  # Deep ocean blue background
        dark_teal = '#034F6D'   # Dark teal buttons
        bright_aqua = '#0ABFD6' # Bright aqua border
        soft_aqua = '#C8F7FF'   # Soft aqua text
        glow_aqua = '#4DF3FF'   # Glow effect
        
        self.figure.patch.set_facecolor(dark_ocean)
        
        self.ax1.clear()
        self.score_data = Database.get_top_10_score()
        sns.barplot(data=self.score_data, x="names", y="scores", ax=self.ax1, color=bright_aqua)
        self.ax1.set_title("Top 10 Scores", color=soft_aqua, fontsize=12, fontweight='bold')
        self.ax1.tick_params(axis='x', rotation=45, colors=soft_aqua, labelsize=9)
        self.ax1.tick_params(axis='y', colors=soft_aqua)
        self.ax1.set_xlabel("names", color=soft_aqua)
        self.ax1.set_ylabel("scores", color=soft_aqua)
        self.ax1.set_facecolor(dark_ocean)
        self.ax1.spines['bottom'].set_color(bright_aqua)
        self.ax1.spines['left'].set_color(bright_aqua)
        self.ax1.spines['top'].set_visible(False)
        self.ax1.spines['right'].set_visible(False)

        self.ax2.clear()
        self.atlantic_wins = Database.get_top_10_atlantic_wins()
        sns.barplot(data=self.atlantic_wins, x="names", y="atlantic wins", ax=self.ax2, color=dark_teal)
        self.ax2.set_title("Top 10 Atlantic Wins", color=soft_aqua, fontsize=12, fontweight='bold')
        self.ax2.tick_params(axis='x', rotation=45, colors=soft_aqua, labelsize=9)
        self.ax2.tick_params(axis='y', colors=soft_aqua)
        self.ax2.set_xlabel("names", color=soft_aqua)
        self.ax2.set_ylabel("atlantic wins", color=soft_aqua)
        self.ax2.set_facecolor(dark_ocean)
        self.ax2.spines['bottom'].set_color(bright_aqua)
        self.ax2.spines['left'].set_color(bright_aqua)
        self.ax2.spines['top'].set_visible(False)
        self.ax2.spines['right'].set_visible(False)

        self.ax3.clear()
        self.pacific_data = Database.get_top_10_pacific_wins()
        sns.barplot(data=self.pacific_data, x="names", y="pacific wins", ax=self.ax3, color=glow_aqua)
        self.ax3.set_title("Top 10 Pacific Wins", color=soft_aqua, fontsize=12, fontweight='bold')
        self.ax3.tick_params(axis='x', rotation=45, colors=soft_aqua, labelsize=9)
        self.ax3.tick_params(axis='y', colors=soft_aqua)
        self.ax3.set_xlabel("names", color=soft_aqua)
        self.ax3.set_ylabel("pacific wins", color=soft_aqua)
        self.ax3.set_facecolor(dark_ocean)
        self.ax3.spines['bottom'].set_color(bright_aqua)
        self.ax3.spines['left'].set_color(bright_aqua)
        self.ax3.spines['top'].set_visible(False)
        self.ax3.spines['right'].set_visible(False)

        self.figure.tight_layout()
        self.canvas.draw()

    def update(self):
        self.refresh_charts()



