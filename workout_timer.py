"""
A module for simulating a training timer
with dynamic time settings.
"""
DEFAULT_TIME = 60

def training_session(rounds: int) -> None:
    """
    Simulates a training session with a given number of rounds.
    """
    time_per_round = DEFAULT_TIME # pylint: disable=global-statement

    def adjust_time(minutes: int) -> None:
        """
        Nested function to change the current round time.
        Uses nonlocal to access a variable in an outer function.
        """

        nonlocal time_per_round
        time_per_round = minutes


    print(f"Start training! Base time: {time_per_round} min.\n")

    for r in range(1, rounds + 1):

        min_round = int(input(f"How many minutes for the {r} round: "))
        adjust_time(min_round)

        print(f"Round {r}: Duration — {time_per_round} min.")

    print("\nTraining completed!")


if __name__ == "__main__":

    number_rounds = int(input("How many rounds would you like to simulate? "))

    training_session(number_rounds)
