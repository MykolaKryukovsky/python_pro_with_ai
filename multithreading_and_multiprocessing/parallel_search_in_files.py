"""
Модуль для паралельного відтворення музики.
Використовує процеси, декоратори та генератори для керування аудіопотоками.
"""
import multiprocessing
import os
import time
import functools
from typing import List, Generator, Any, Callable

import pygame


def mixer_lifecycle(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator for automatic initialization and graceful termination
    of the audio mixer in a separate process.
    """
    @functools.wraps(func)
    def wrapper(self: 'SongPlayer', *args: Any, **kwargs: Any) -> Any:
        try:
            pygame.mixer.init()
            result = func(self, *args, **kwargs)
            while pygame.mixer.music.get_busy():
                time.sleep(0.2)
            return result
        except (pygame.error, FileNotFoundError, OSError) as e: # pylint: disable=no-member
            print(f"[ERROR] Помилка аудіо у файлі {os.path.basename(self.file_path)}: {e}")
            return None
        finally:
            pygame.mixer.quit()

    return wrapper


class SongPlayer: # pylint: disable=too-few-public-methods
    """A class for playing a single track."""
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path

    @mixer_lifecycle
    def play(self) -> None:
        """Plays an audio file (controlled by a decorator)."""
        pygame.mixer.music.load(self.file_path)
        pygame.mixer.music.play()
        print(f"[PLAYING] Одночасне звучання: {os.path.basename(self.file_path)}")


class ConcertHall:
    """A class for controlling multiple players in parallel."""
    def __init__(self, playlist: List[str]) -> None:
        self.playlist: List[str] = playlist
        self.processes: List[multiprocessing.Process] = []

    def get_valid_tracks(self) -> Generator[str, None, None]:
        """
        A generator that filters a playlist and
        returns only existing files.
        """
        for track in self.playlist:
            if os.path.exists(track):
                yield track
            else:
                print(f"[SKIP] Файл не знайдено: {track}")

    def start_concert(self) -> None:
        """Plays all songs in parallel via the track generator."""
        for track_path in self.get_valid_tracks():
            player = SongPlayer(track_path)
            process = multiprocessing.Process(target=player.play)
            self.processes.append(process)
            process.start()

        for p in self.processes:
            p.join()
        print("\n[INFO] Всі пісні закінчилися.")


if __name__ == "__main__":

    my_songs = ["rock_star.mp3", "jazz_vibes.wav", "ambient.mp3"]

    hall = ConcertHall(my_songs)
    hall.start_concert()
