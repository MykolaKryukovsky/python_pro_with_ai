"""
This module provides a PostgreSQL user management system.
It handles user creation and database schema initialization.
"""
from typing import Optional
import psycopg2
from psycopg2 import Error


class PostgresUserManager:
    """
    Manages user-related operations in a PostgreSQL database.
    Attributes:
        conn: The PostgreSQL connection object.
        cur: The database cursor for executing queries.
    """
    def __init__(self) -> None:
        """Initializes the connection and sets up the users table."""
        try:
            self.conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="123",
                host="localhost"
            )
            self.cur = self.conn.cursor()
            self._setup_db()
        except Error as e:
            print(f"PostgreSQL підключення не вдалося: {e}")
            raise

    def _setup_db(self) -> None:
        """Creates the users table if it does not already exist."""
        self.cur.execute("CREATE TABLE IF NOT EXISTS "
                "users (id SERIAL PRIMARY KEY, name TEXT, email TEXT)"
        )
        self.conn.commit()

    def create_user(self, name: str, email: str) -> Optional[int]:
        """
        Inserts a new user and returns their unique ID.
        Args:
            name (str): The name of the user.
            email (str): The email address of the user.
        Returns:
            Optional[int]: The newly created user ID or None if failed.
        """
        try:
            query = "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id"
            self.cur.execute(query, (name, email))
            user_id = self.cur.fetchone()[0]
            self.conn.commit()
            print(f"Користувач {name} створено за допомогою ID: {user_id}")
            return user_id
        except Error as e:
            self.conn.rollback()
            print(f"Не вдалося створити користувача: {e}")
            return None

    def close(self) -> None:
        """Closes the cursor and the database connection."""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
            print("PostgreSQL з'єднання закрито.")
