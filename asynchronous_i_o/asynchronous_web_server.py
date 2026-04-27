"""
This module demonstrates a simple asynchronous web server using aiohttp.
It handles basic routing and non-blocking delays.
"""
import asyncio
from aiohttp import web


async def handle_root(_request: web.Request) -> web.Response:
    """
    Handles the root route.
    Returns a simple 'Hello, World!' text.
    """
    return web.Response(text="Hello, World!")


async def handle_slow(_request: web.Request) -> web.Response:
    """
    Simulates a long-running operation with a 5-second delay.
    Does not block the server from handling other requests.
    """
    print("Slow request started...")
    await asyncio.sleep(5)
    print("Slow request finished.")
    return web.Response(text="Operation completed")


async def make_app() -> web.Application:
    """
    Creates and configures the web application with routes.
    """
    app = web.Application()
    app.add_routes([
        web.get('/', handle_root),
        web.get('/slow', handle_slow)
    ])
    return app


if __name__ == "__main__":

    web.run_app(make_app(), port=8080)
