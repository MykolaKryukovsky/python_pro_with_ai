"""
A module for managing event calendars through locking.
"""
happenings = []

def create_calendar() -> tuple:

    def adding_events(event: str) -> None:
        """Adds a new event to the global list."""

        happenings.append(event)
        print(f"Event '{event}' added.")

    def deleting_events(event: str) -> None:
        """Deletes an event by name, if it exists."""

        if event in happenings:
            happenings.remove(event)
            print(f"Event '{event}' deleted")
        else:
            print(f"Event {event} not found!")

    def viewing_upcoming_events(events: list) -> None:
        """Lists all upcoming events."""

        if not events:
            print("Calendar is empty.")
        else:
            print(f"List of upcoming events: {events}")


    return adding_events, deleting_events, viewing_upcoming_events


if __name__ == "__main__":

    add_ev, del_ev, view_ev = create_calendar()

    some_ev = input("Enter event: ")
    add_ev(some_ev)

    some_ev = input("Enter event: ")
    add_ev(some_ev)

    some_ev = input("Enter event: ")
    add_ev(some_ev)

    view_ev (happenings)

    some_ev = input("Enter the event you want to delete: ")
    del_ev(some_ev)

    view_ev(happenings)
