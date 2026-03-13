"""
A module for working with data about people.
Includes a Person class with the ability to compare by age.
"""
class Person:
    """
    Represents a person with a name and age.
    """

    objects_ls = []

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.objects_ls.append(self)
        Person.objects_ls.sort(key=lambda x: x.age, reverse=True)


    def __lt__(self, other: Person) -> bool:
        return self.age < other.age

    def __gt__(self, other: Person) -> bool:
        return self.age > other.age

    def __eq__(self, other: Person) -> bool:
        return self.age == other.age

    def __repr__(self):
        return f"\nPerson({self.name}, age: {self.age})"


if __name__ == "__main__":

    p1 = Person("Вася", 30)
    p2 = Person("Таня", 20)
    p3 = Person("Петро", 40)
    p4 = Person("Ирина", 50)
    p5 = Person("Саша", 100)

    print(p1 > p2)
    print(p3 < p2)
    print(p5 == p4)
    print(p4 < p2)
    print(p1 == p5)

    print(Person.objects_ls)
