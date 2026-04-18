import sqlite3
import os

from data.state import state

class Database:
    def __init__(self):
        self.file_path = os.path.join("data", "Protect_Franklin_The_Turtle.db")
        self.connection = sqlite3.connect(self.file_path)
        self.cursor = self.connection.cursor()
        self.make_tables()

    def make_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS game_state(
                id INTEGER PRIMARY KEY,
                score INTEGER,
                lives INTEGER,
                alantic_wins INTEGER,
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
        self.cursor.execute("""INSERT INTO game_state (score, lives, alantic_wins, pacific_wins, name) 
                            VALUES (?,?,?,?,?)""", (data["score"], data["lives"], data["alantic_wins"], data["pacific_wins"], data["name"],))
        self.connection.commit()

    def get_d_by_name(self, name:str) -> dict:
        self.cursor.execute("""SELECT * FROM game_state where name = ?""", (name,))
        data = self.cursor.fetchone()
        if data:
            return {
                "score": data[1],
                "lives": data[2],
                "alantic_wins": data[3],
                "pacific_wins": data[4],
                "name": data[5]
            }
        return state()

    @staticmethod
    def insert_data(data:dict):
        with Database() as d:
            d.in_data(data)

    @staticmethod
    def get_data_by_name(name:str) -> dict:
        with Database() as d:
            data = d.get_d_by_name(name)
        return data


