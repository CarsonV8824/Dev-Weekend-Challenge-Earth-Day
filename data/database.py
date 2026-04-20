import sqlite3
import os

import pandas as pd

from data.state import state

# Get project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Database:
    def __init__(self):
        self.file_path = os.path.join(PROJECT_ROOT, "data", "Franklin_and_the_Diver.db")
        self.connection = sqlite3.connect(self.file_path)
        self.cursor = self.connection.cursor()
        self.make_tables()

    def make_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS game_state(
                id INTEGER PRIMARY KEY,
                score INTEGER,
                lives INTEGER,
                atlantic_wins INTEGER,
                pacific_wins INTEGER,
                name TEXT         
                );
        """)
        self.connection.commit()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def in_data(self, data:dict) -> None:
        self.cursor.execute("""INSERT INTO game_state (score, lives, atlantic_wins, pacific_wins, name) 
                            VALUES (?,?,?,?,?)""", (data["score"], data["lives"], data["atlantic_wins"], data["pacific_wins"], data["name"],))
        self.connection.commit()

    def get_d_by_name(self, name:str) -> dict:
        self.cursor.execute("""SELECT * FROM game_state where name = ?""", (name,))
        data = self.cursor.fetchone()
        if data:
            return {
                "score": data[1],
                "lives": data[2],
                "atlantic_wins": data[3],
                "pacific_wins": data[4],
                "name": data[5]
            }
        return state()
    
    @staticmethod
    def get_top_10_score() -> pd.DataFrame:
        with Database() as d:
            d.cursor.execute("""SELECT name, MAX(score) as score FROM game_state GROUP BY name ORDER BY MAX(score) DESC LIMIT 10""")
            data = d.cursor.fetchall()
            # Create dataframe directly from fetched data
            dataframe = pd.DataFrame(data, columns=["names", "scores"])
        return dataframe
    
    @staticmethod
    def get_top_10_atlantic_wins() -> pd.DataFrame:
        with Database() as d:
            d.cursor.execute("""SELECT name, MAX(atlantic_wins) as atlantic_wins FROM game_state GROUP BY name ORDER BY MAX(atlantic_wins) DESC LIMIT 10""")
            data = d.cursor.fetchall()
            dataframe = pd.DataFrame(data, columns=["names", "atlantic wins"])
        return dataframe
    
    @staticmethod
    def get_top_10_pacific_wins():
        with Database() as d:
            d.cursor.execute("""SELECT name, MAX(pacific_wins) as pacific_wins FROM game_state GROUP BY name ORDER BY MAX(pacific_wins) DESC LIMIT 10""")
            data = d.cursor.fetchall()
            dataframe = pd.DataFrame(data, columns=["names", "pacific wins"])
        return dataframe

    @staticmethod
    def insert_data(data:dict):
        with Database() as d:
            d.in_data(data)

    @staticmethod
    def get_data_by_name(name:str) -> dict:
        with Database() as d:
            data = d.get_d_by_name(name)
        return data


