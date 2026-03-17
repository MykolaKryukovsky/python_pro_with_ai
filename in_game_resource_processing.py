"""
A module for managing player resources and handling resource shortage errors.
"""
class InsufficientResourcesException(Exception):
    """Exception raised for insufficient resources."""

    def __init__(self, required_resource: str, required_amount: int, current_amount: int) -> None:
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount
        self.missing_amount = required_amount - current_amount
        message = (f"Game Required-Resource: {required_resource} "
                   f"| Required-Amount: {required_amount}"
                   f" | Current-Amount: {current_amount} "
                   f"| Missing-Amount: {self.missing_amount}"
        )
        super().__init__(message)


class GameResource:
    """A class that simulates game actions with resources."""

    def __init__(self, gold: int, mana: int ) -> None:
        self.resources = { 'gold': gold, 'mana': mana }

    def buy_item(self, item_name: str, cost: int) -> None:
        """Attempting to buy an item with gold."""

        print(f"\n🛒 Trying to buy '{item_name}' for {cost} gold...")

        if self.resources['gold'] < cost:
            raise InsufficientResourcesException("Gold", cost, self.resources['gold'])

        self.resources['gold'] -= cost

        print(f"✅ Success! '{item_name}' purchased. Gold remaining: {self.resources['gold']}")


    def cast_spell(self, spell_name: str, mana_cost: int) -> None:
        """Attempt a magical action for mana."""

        print(f"\n🔮 Attempting to cast '{spell_name}' (cost: {mana_cost} mana)...")

        if self.resources['mana'] < mana_cost:
            raise InsufficientResourcesException("Mana", mana_cost, self.resources['mana'])

        self.resources['mana'] -= mana_cost

        print(f"✨ Magic! '{spell_name}' activated. Remaining mana: {self.resources['mana']}")


if __name__ == "__main__":

    player = GameResource(gold = 500, mana = 200)

    actions = [ lambda: player.buy_item("Health potion", 100),
               lambda: player.buy_item("Legendary blade", 500),
               lambda: player.cast_spell("Fiery layers", 50)
    ]

    for action in actions:
        try:
            action()
        except InsufficientResourcesException as e:
            print(f"❌ ERROR: {e}")
            print(f"Hint: You need {e.missing_amount} "
                  f"more units of the resource '{e.required_resource}'."
            )
