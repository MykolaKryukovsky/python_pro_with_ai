"""
This module contains helper functions to handle user interactions
and coordinate database operations for the MovieBase application.
"""


def handle_add_actor(app):
    """Handles logic for adding a new actor."""
    name = input("Actor's name: ")
    year = int(input("Year of birth: "))
    app.add_actor(name, year)


def handle_unique_genres(app):
    """Retrieves and prints unique genres from the database."""
    print("\n--- Unique Movie Genres ---")
    genres = app.get_unique_genres()
    if not genres:
        print("No movies found, so no genres available.")
    else:
        for genre in genres:
            print(f"- {genre[0]}")


def handle_add_movie(app):
    """Handles logic for adding a movie and linking actors."""
    print("\nAvailable actors:")
    actors = app.cursor.execute("SELECT id, name FROM actors").fetchall()

    if not actors:
        print("No actors found! Please add an actor first.")
        return

    for actor in actors:
        print(f"ID: {actor[0]} | Name: {actor[1]}")

    title = input("Movie title: ")
    year = int(input("Release year: "))
    genre = input("Genre: ")
    ids_str = input("Enter actor IDs (e.g.: 1,2): ")
    actor_ids = [int(i.strip()) for i in ids_str.split(",") if i.strip()]
    app.add_movie(title, year, genre, actor_ids)


def handle_search_and_stats(app, choice):
    """Handles search, age calculation and statistics."""
    if choice == 4:
        word = input("Search keyword: ")
        movies = app.search_by_title(word)
        for m in movies:
            print(f"ID: {m[0]} | Title: {m[1]} ({m[2]})")
    elif choice == 5:
        for title, age in app.get_movies_with_age():
            print(f"{title}: {age} years old")
    elif choice == 6:
        for genre, count in app.count_movies_by_genre():
            print(f"Genre: {genre} | Count: {count}")


def handle_deletion(app, choice):
    """Handles deletion of movies or actors."""
    if choice == 8:
        movies = app.cursor.execute("SELECT id, title FROM movies").fetchall()
        for m in movies:
            print(f"ID: {m[0]} | Title: {m[1]}")
        mid = int(input("Enter Movie ID to delete: "))
        app.delete_movie(mid)
    elif choice == 9:
        actors = app.cursor.execute("SELECT id, name FROM actors").fetchall()
        for a in actors:
            print(f"ID: {a[0]} | Name: {a[1]}")
        aid = int(input("Enter Actor ID to delete: "))
        app.delete_actor(aid)
