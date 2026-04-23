"""
A multi-threaded web server module.
Implements processing of HTTP requests using ThreadingMixIn,
decorators and introspection.
"""
import http.server
import socketserver
import inspect
import functools
from datetime import datetime
from typing import Callable, Any, Generator


def log_request(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that logs the current timestamp and request path before processing.
    Args:
    func (callable): The handler method to be decorated (e.g., do_GET).
    Returns:
    callable: The wrapped function with logging capabilities.
    """
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"[LOG] {datetime.now()}: Обробка запиту {self.path}")
        return func(self, *args, **kwargs)
    return wrapper


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom HTTP request handler with introspection and advanced logging.
    """
    def data_receiver(self) -> Generator[str, None, None]:
        """
        A generator that reads the request body if Content-Length is provided.
        Yields:
        str: Decoded UTF-8 string containing a chunk of the request body.
        """
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            yield self.rfile.read(content_length).decode('utf-8')

    @log_request
    def do_GET(self) -> None:
        """
        Handles GET requests, performs introspection, and serves a dynamic HTML response.
        """
        try:
            if self.path == "/admin":
                self.send_error(403, "Access Denied")
            else:
                self.show_reflection()

                received_data = "".join(self.data_receiver())

                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()

                response_gen = (part for part in [
                    "<html><body>",
                    "<h1>Привіт від багатопотокового сервера!</h1>",
                    f"<p>Шлях: {self.path}</p>",
                    f"<p>Отримані дані: {received_data if received_data else 'немає'}</p>",
                    "</body></html>"
                ])

                for fragment in response_gen:
                    self.wfile.write(fragment.encode('utf-8'))

        except (ConnectionResetError, BrokenPipeError) as network_err:
            print(f"[ERROR] Мережева помилка: {network_err}")
            self.send_error(500, "Internal Server Error")
        except UnicodeDecodeError as decode_err:
            print(f"[ERROR] Помилка кодування: {decode_err}")
            self.send_error(400, "Bad Request: Unicode Decode Error")
        except OSError as sys_err:
            print(f"[SYSTEM ERROR] Системна помилка сокета: {sys_err}")
            self.send_error(500, "Internal Server Error")

    def show_reflection(self) -> None:
        """
        Performs introspection on the do_GET method using getattr and inspect.
        """
        method = getattr(self, "do_GET")
        print(f"[REFLECT] Метод: {method.__name__}, Аргументи: {inspect.signature(method)}")


class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    """
    HTTP Server that handles each request in a separate thread.
    Uses ThreadingMixIn for concurrency and performs server-level introspection.
    """
    def server_activate(self) -> None:
        """
        Overrides server_activate to print server class hierarchy before starting.
        """
        print("--- Интроспекція сервера ---")
        print(f"Класс: {self.__class__.__name__}")
        print(f"Ієрархія: {[c.__name__ for c in inspect.getmro(self.__class__)]}")
        super().server_activate()


if __name__ == "__main__":

    HOST, PORT = '', 8080

    with ThreadedHTTPServer((HOST, PORT), CustomHandler) as httpd:
        print(f"Сервер запущено на порту{PORT}...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nСервер зупинено.")
