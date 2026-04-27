"""
This module demonstrates the Producer-Consumer pattern using asyncio.Queue.
It shows how to distribute tasks among multiple concurrent workers.
"""
import asyncio


async def producer(queue: asyncio.Queue) -> None:
    """
    Generates tasks and adds them to the queue.
    Args:
    queue (asyncio.Queue): The queue to put tasks into.
    """
    for i in range(1, 6):
        await asyncio.sleep(1)
        task = f"Task #{i}"
        await queue.put(task)
        print(f"[Producer] Produced: {task}")

    print("[Producer] Finished producing all tasks.")


async def consumer(name: str, queue: asyncio.Queue) -> None:
    """
    Retrieves tasks from the queue and processes them.
    Args:
    name (str): The name of the consumer (worker).
    queue (asyncio.Queue): The queue to get tasks from.
    """
    while True:
        task = await queue.get()
        print(f"[Consumer {name}] Started processing: {task}")
        await asyncio.sleep(2)
        print(f"[Consumer {name}] Finished processing: {task}")
        queue.task_done()


async def main():
    """
    Coordinates the producer and multiple consumers.
    """
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))

    consumers = [asyncio.create_task(consumer(f"Worker-{i}", queue))
                 for i in range(1, 3)
    ]
    await producer_task
    await queue.join()
    for c in consumers:
        c.cancel()

    print("\n[Main] All tasks have been processed System shut down.")


if __name__ == "__main__":

    asyncio.run(main())
