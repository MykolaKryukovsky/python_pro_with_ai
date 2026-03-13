"""
A module for comparing three approaches to working with attributes:
getters/setters, the @property decorator, and descriptors.
"""

class PriceDescriptor:
    """Descriptor to check the price (extracted separately for reuse)."""

    def __get__(self, instance: object, owner: object) -> float:
        return getattr(instance, '_price', 0.0)

    def __set__(self, instance, price) -> None:
        if  price < 0:
            raise ValueError("The price cannot be negative")
        instance._price = float(price)

class CurrencyDescriptor:
    """Descriptor for currency management and automatic price conversion."""

    def __init__(self):
        self.rates = {'UAH': 1.0, 'USD': 45.0, 'EUR': 50.0}

    def __get__(self, instance: object, owner: object) -> float:
        return getattr(instance, '_currency', 'UAH')

    def __set__(self, instance: object, currency_code: str) -> None:

        if currency_code not in self.rates:
            raise ValueError("Currency code must be one of UAH, USD, EUR")

        if hasattr(instance, '_price'):
            old_currency = getattr(instance, '_currency', 'UAH')
            new_price = (instance.price * self.rates[old_currency]) / self.rates[currency_code]
            instance.price = new_price

        instance._currency = currency_code



class Product:
    """Class container for comparing three methods of working with attributes."""

    def __init__(self, name: str) -> None:
        self._name = name

    def __repr__(self) -> str:
        return f"{self._name}"

    class WithGetSet:
        """Option 1: Classic getters and setters."""

        def __init__(self, name: str, price: float) -> None:
            self._name = name
            self.set_price(price)

        def get_price(self) -> float:
            """Initialization via set_price method."""
            return self._price

        def set_price(self, price) -> None:
            """Method for setting a price with validation."""
            if price < 0:
                raise ValueError("The price cannot be negative")
            self._price = float(price)

        def __repr__(self) -> str:
            return f"{self._name}"

    class WithProperty:
        """Option 2: @property decorator."""

        def __init__(self, name: str, price: float) -> None:
            self._name = name
            self.price = price

        @property
        def price(self) -> float:
            """Getter for the cost."""

            return self._price

        @price.setter
        def price(self, price: float) -> None:
            if price < 0:
                raise ValueError("The price cannot be negative")
            self._price = float(price)

        def __repr__(self) -> str:
            return f"{self._name}"

    class WithDescriptor:
        """Option 3: Descriptors."""

        price_wd = PriceDescriptor()

        def __init__(self, name: str, price: float) -> None:
            self._name = name
            self.price_wd = price

        def __repr__(self):
            return f"{self._name}"

    class WithCurrency:
        """A product that uses descriptors for price and currency."""

        price = PriceDescriptor()
        currency = CurrencyDescriptor()

        def __init__(self, name: str, price: float, currency: str = 'UAH'):
            self.name = name
            self._currency = currency
            self.price = price

        def __repr__(self):
            return f"Product: {self.name} | Price: {self.price:.2f} {self.currency}"



if __name__ == "__main__":

    p1 = Product.WithGetSet("Apples", 80.0)
    p2 = Product.WithProperty("Milk", 120.0)
    p3 = Product.WithDescriptor("Bread", 45.0)
    p4 = Product.WithCurrency("Bananas", 70, 'UAH')

    print(f" Price:\n {p1} {p1.get_price()} \n {p2} {p2.price} \n {p3} {p3.price_wd} \n {p4} ")

    p4.currency = 'EUR'

    print(f" After changing to EUR: {p4}")
