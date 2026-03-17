"""
The module for processing game events through the system is excluded.
Contains classes for generating, logging and processing game situations.
"""
class GameEventException(Exception):
    """Custom class for handling game events through the exception mechanism."""

    def __init__(self, event_type: str, details: dict) -> None:
        self.event_type = event_type
        self.details = details
        message = f"Game Event: {event_type} | Details: {details}"
        super().__init__(message)


class GameEventProcessing:
    """A class for generating and processing game events."""

    def __init__(self, player_name: str) -> None:
        self.player_name = player_name
        self.events = []

    def exception_event(self, scenario: str):
        """Emulation of game situations that cause exceptions."""

        if scenario == "trap":
            raise GameEventException(
                event_type = "death",
                details = {"reason": "cosmic radiation", "location": "black hole", "loss_exp": 100}
            )

        if scenario == "quest_complete":
            raise GameEventException(
                event_type = "levelUp",
                details = {"new_level": 10, "exp_gained": 1500, "bonus_item": "Kinetic weapon"}
            )

        print(f"Normal movement of player {self.player_name}...")

    def process_game(self, scenario: str):
        """A 'try-catch' method for handling events."""

        try:
            self.exception_event(scenario)

        except GameEventException as event:
            self._log_event(event)  # Сохраняем в историю

            if event.event_type == "death":
                print(f"💀 Player {self.player_name} "
                      f"is dead! Reason: {event.details['reason']}."
                )
                print(f"You lost {event.details['loss_exp']} "
                      f"experience in location {event.details['location']}."
                )

            elif event.event_type == "levelUp":
                print(f"✨ LEVEL UP! New level: {event.details['new_level']}.")
                print(f"Gained: {event.details['exp_gained']} "
                      f"XP and item: {event.details['bonus_item']}."
                )

    def _log_event(self, event: GameEventException):
        """Internal method for recording event history."""

        entry = {"type": event.event_type, "data": event.details}
        self.events.append(entry)
        print(f"[System]: Event '{event.event_type}' recorded in the database.")


if __name__ == "__main__":

    game = GameEventProcessing("Marcus")

    game.process_game("quest_complete")
    game.process_game("trap")
