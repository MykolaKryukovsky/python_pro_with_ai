"""
A module for tracking expenses using global variables.
"""
TOTAL_EXPENSE = 0.0

def  add_expense(spending: float) -> None:
    """Adds the cost amount to the total."""

    global TOTAL_EXPENSE # pylint: disable=global-statement

    if spending > 0:
        TOTAL_EXPENSE += spending
        print(f"Expense {spending:.2f} added successfully.")
    else:
        print("Error: sum must be greater than zero.")

def get_expense() -> float:
    """Returns the current total cost."""

    return TOTAL_EXPENSE


if __name__ == "__main__":

    print("EXPENSE TRACKER")

    while True:
        print("\nSelect an action:")
        print("A. Add expense")
        print("B. View total")
        print("C. Exit")

        choice = input("Your choice (A, B, C): ")

        if choice == "A":
            try:
                value = float(input("Enter the expense amount: "))
                add_expense(value)
            except ValueError:
                print("Error: Please enter a number.")

        elif choice == "B":
            print(f"Your total expenses: {get_expense():.2f}")

        elif choice == "C":
            print("The program is over. Have a nice day!")
            break

        else:
            print("Incorrect choice, try again.")
