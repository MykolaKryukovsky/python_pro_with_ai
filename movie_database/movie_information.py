"""
This module provides a class for managing a movie database using SQLite.
It includes table creation for movies, actors, and their relationships.
"""

import sqlite3
from datetime import datetime


def movie_age(release_year):
    """
    Calculates the age of a movie based on the current year.
    """
    current_year = datetime.now().year
    return current_year - release_year


class MovieInformation:
    """
    A class to handle the core database operations for the MovieBase application.
    """

    def __init__(self, db_filename="") -> None:
        try:
            self.conn = sqlite3.connect(db_filename)
            self.conn.execute('''PRAGMA foreign_keys = ON;''')
            self.conn.create_function("movie_age", 1, movie_age)
            self.cursor = self.conn.cursor()
            print(f"Successful connection to {db_filename}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")


    def movie(self) -> None:
        """
        Creates the 'movies' table if it does not already exist.
        """
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    release_year INTEGER,
                    genre TEXT
                )
            ''')
            self.conn.commit()
            print("Table 'movies' is ready.")
        except sqlite3.Error as e:
            print(f"Error when creating the 'movies' table: {e}")

    def actors(self) -> None:
        """
        Creates the 'actors' table if it does not already exist.
        """
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS actors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    birth_year INTEGER
                )
            ''')
            self.conn.commit()
            print("The 'actors' table is ready.")
        except sqlite3.Error as e:
            print(f"Error when creating the 'actors' table: {e}")

    def movie_cast(self) -> None:
        """
        Creates the 'movie_cast' junction table for many-to-many relationships.
        """
        try:
            self.cursor.execute('''
                 CREATE TABLE IF NOT EXISTS movie_cast (
                    movie_id INTEGER,
                    actor_id INTEGER,
                    PRIMARY KEY(movie_id, actor_id),
                    FOREIGN KEY(movie_id) REFERENCES movies(id) ON DELETE CASCADE,
                    FOREIGN KEY(actor_id) REFERENCES actors(id) ON DELETE CASCADE
                )
            ''')
            self.conn.commit()
            print("The 'movie_cast' table is ready.")
        except sqlite3.Error as e:
            print(f"Error when creating the 'movie_cast' table: {e}")

    def close(self) -> None:
        """
        Closes the database connection safely.
        """
        try:
            self.conn.close()
            print("The connection to the database is closed.")
        except sqlite3.Error as e:
            print(f"Error when closing the database: {e}")
