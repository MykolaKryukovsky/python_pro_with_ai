"""
This module provides extended functionality for the movie database.
It includes methods for data manipulation, search, aggregation, and deletion.
"""

# pylint: disable=import-error
import sqlite3
import movie_information as im


class MovieFunctionality(im.MovieInformation):
    """
    Handles advanced database operations such as adding, deleting,
    and querying movie-related data.
    """

    def add_movie(self, title: str, year: int, genre: str, actor_ids: str) -> None:
        """
        Adds a new movie and links it with multiple actors.
        """
        try:
            self.cursor.execute("""
                INSERT INTO movies (title, release_year, genre) 
                VALUES (?,?,?)""", (title, year, genre)
            )

            movie_id = self.cursor.lastrowid

            for a_id in actor_ids:
                self.cursor.execute("""
                    INSERT INTO movie_cast (movie_id, actor_id) 
                    VALUES (?, ?)""", (movie_id, a_id)
                )
            self.conn.commit()
            print(f"Movie '{title}' successfully added.")
        except sqlite3.Error as e:
            print(f"Error while adding movie: {e}")

    def add_actor(self, name: int, birth_year: int) -> None:
        """
        Adds a new actor to the database.
        """
        try:
            self.cursor.execute("""
                    INSERT INTO actors (name, birth_year) 
                    VALUES (?, ?)""", (name, birth_year)
            )
            self.conn.commit()
            print(f"Actor '{name}' successfully added.")
        except sqlite3.Error as e:
            print(f"Error while adding actor: {e}")

    def get_movies_with_actors(self) -> list:
        """
        Returns a list of movies with all assigned actors using INNER JOIN.
        """
        try:
            query = '''
                        SELECT m.title, GROUP_CONCAT(a.name, ', ')
                        FROM movies m
                        INNER JOIN movie_cast mc ON m.id = mc.movie_id
                        INNER JOIN actors a ON mc.actor_id = a.id
                        GROUP BY m.id
                    '''
            return self.cursor.execute(query).fetchall()
        except sqlite3.Error as e:
            print(f"Error while getting movies with actors: {e}")
            return []

    def get_unique_genres(self) -> list:
        """
        Retrieves a unique list of movie genres using DISTINCT.
        """
        return self.cursor.execute("SELECT DISTINCT genre FROM movies").fetchall()

    def count_movies_by_genre(self) -> list:
        """
        Counts the number of movies for each genre using COUNT and GROUP BY.
        """
        query = "SELECT genre, COUNT(*) FROM movies GROUP BY genre"
        return self.cursor.execute(query).fetchall()

    def avg_actor_birth_year_by_genre(self, genre: str) -> int:
        """
        Calculates the average birth year of actors in a specific genre using AVG.
        """
        try:
            query = '''
                        SELECT AVG(a.birth_year)
                        FROM actors a
                        JOIN movie_cast mc ON a.id = mc.actor_id
                        JOIN movies m ON mc.movie_id = m.id
                        WHERE m.genre = ?
                    '''
            return self.cursor.execute(query, (genre,)).fetchone()[0]
        except sqlite3.Error as e:
            print(f"Error while getting average birth year for genre: {e}")
            return 0

    def search_by_title(self, keyword: str) -> list:
        """
        Searches for movies containing the keyword in their title using LIKE.
        """
        return self.cursor.execute("SELECT * FROM movies WHERE title LIKE ?",
                                (f'%{keyword}%',)).fetchall()

    def get_movies_paginated(self, limit: int, offset: int) -> list:
        """
        Returns a limited list of movies for pagination using LIMIT and OFFSET.
        """
        return self.cursor.execute("SELECT * FROM movies LIMIT ? OFFSET ?",
                                (limit, offset)).fetchall()

    def get_all_names_and_titles(self) -> list:
        """
        Returns a combined list of all actor names and movie titles using UNION.
        """
        return self.cursor.execute("SELECT title AS name FROM movies "
                                "UNION SELECT name FROM actors").fetchall()

    def get_movies_with_age(self) -> list:
        """
        Returns movie titles with their age calculated by a custom SQL function.
        """
        query = "SELECT title, movie_age(release_year) FROM movies"
        return self.cursor.execute(query).fetchall()

    def delete_movie(self, movie_id: int) -> None:
        """
        Deletes a movie by ID. Cascade deletion handles the 'movie_cast' table.
        """
        try:
            self.cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
            self.conn.commit()
            print(f"Movie with ID {movie_id} deleted.")
        except sqlite3.Error as e:
            print(f"Error deleting movie: {e}")

    def delete_actor(self, actor_id: int) -> None:
        """
        Deletes an actor from the database by ID.
        """
        try:
            self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
            self.conn.commit()
            print(f"Actor with ID {actor_id} deleted.")
        except sqlite3.Error as e:
            print(f"Error deleting actor: {e}")
