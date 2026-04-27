"""
This module demonstrates how to handle timeouts in asynchronous tasks.
It uses asyncio.wait_for to cancel a task that takes too long to execute.
"""
import asyncio


async def slow_task() -> str:
    """
    Simulates a long-running task that takes 10 seconds to complete.
    """
    print("Slow task: Started, will take 10 seconds...")
    await asyncio.sleep(10)
    print("Slow task: Finished successfully!")
    return "Result"


async def main():
    """
    Calls a slow task with a 5-second timeout and handles the potential timeout.
    """
    timeout_limit = 5

    try:
        print(f"Main: Starting task with timeout of {timeout_limit} seconds...")
        await asyncio.wait_for(slow_task(), timeout=timeout_limit)
        print("Main: Task completed within the time limit.")
    except TimeoutError:
        print(f"Main: Error! The task exceeded the {timeout_limit} seconds timeout.")


if __name__ == "__main__":

    asyncio.run(main())
