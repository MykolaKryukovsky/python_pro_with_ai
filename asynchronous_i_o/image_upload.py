"""
Asynchronous image scraper with aiosqlite database integration.
"""
import asyncio
import os
from typing import Any

import aiohttp
import aiofiles
import aiosqlite


async def init_db(db: aiosqlite.Connection) -> None:
    """Initializes the database schema using the existing connection."""
    await db.execute("""
        CREATE TABLE IF NOT EXISTS downloads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            filename TEXT,
            status INTEGER
        )
    """)
    await db.commit()


async def download_image(session: Any, db: Any , url: str, folder: str , name: str) -> None:
    """Downloads an image and logs it using the shared DB connection."""
    filename = os.path.join(folder, name)

    try:
        async with session.get(url, timeout=5) as response:
            status = response.status
            if status == 200:
                content = await response.read()
                async with aiofiles.open(filename, mode='wb') as f:
                    await f.write(content)
                print(f"Saved and Logged: {name}")
            else:
                print(f"HTTP Error {status}: {name}")
    except aiohttp.ClientConnectorError:
        print(f"Connection error: {url} is unavailable.")
    except asyncio.TimeoutError:
        print(f"Waiting time expired for {url}.")
    except aiohttp.InvalidURL:
        print(f"Invalid format URL: {url}.")
        status = -1

    await db.execute(
        "INSERT INTO downloads (url, filename, status) VALUES (?, ?, ?)",
        (url, filename, status)
    )
    await db.commit()


async def main():
    """
    Main entry point for the image scraper.
    Initializes the database connection, sets up the storage folder,
    and manages the concurrent execution of download tasks.
    """
    folder = "downloads"

    if not os.path.exists(folder):
        os.makedirs(folder)

    async with aiosqlite.connect("images.db") as db, \
            aiohttp.ClientSession() as session:

        await init_db(db)

        images = [
            ("https://placeholder.com", "img1.png"),
            ("https://placeholder.com", "img2.png"),
            ("https://placeholder.com", "img3.png")
        ]

        tasks = [
            download_image(session, db, url, folder, name)
            for url, name in images
        ]

        await asyncio.gather(*tasks)

        async with db.execute("SELECT COUNT(*) FROM downloads") as cursor:
            count = await cursor.fetchone()
            print(f"\nTotal records in DB: {count[0]}")


if __name__ == "__main__":

    asyncio.run(main())
