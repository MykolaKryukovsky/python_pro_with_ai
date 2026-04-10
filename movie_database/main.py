"""
This is the main entry point for the MovieBase console application.
It provides a user interface to interact with the movie database.
"""

# pylint: disable=import-error
import sqlite3
import movie_functionality
import database_function as df


def main() -> None:
    """Main application loop."""
    app = movie_functionality.MovieFunctionality("kinobaza.db")
    app.movie()
    app.actors()
    app.movie_cast()

    while True:

        print("\n--- MOVIEBASE MENU ---")
        print("1. Add actor")
        print("2. Add movie and assign actors")
        print("3. List of movies with actors (JOIN)")
        print("4. Search for a movie by title (LIKE)")
        print("5. Age of movies (Custom function + ORDER BY)")
        print("6. Statistics: Number of movies by genre (COUNT)")
        print("7. Show unique genres (DISTINCT)")
        print("8. Delete movie")
        print("9. Delete actor")
        print("0. Exit")

        try:
            choice = int(input("Choice: "))

            if choice == 1:
                df.handle_add_actor(app)
            elif choice == 2:
                df.handle_add_movie(app)
            elif choice == 3:
                for m, c in app.get_movies_with_actors():
                    print(f"Movie: {m} | Actors: {c}")
            elif 4 <= choice <= 6:
                df.handle_search_and_stats(app, choice)
            elif choice == 7:
                df.handle_unique_genres(app)
            elif 8 <= choice <= 9:
                df.handle_deletion(app, choice)
            elif choice == 0:
                app.close()
                print("Bye!")
                break
            else:
                print("Invalid choice! Use 0-8.")
        except (ValueError, sqlite3.Error) as error:
            print(f"Error: {error}")


if __name__ == '__main__':

    main()
