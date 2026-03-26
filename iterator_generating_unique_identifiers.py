"""Module for generating unique UUID4 identifiers using an iterator."""
import uuid

class UniqueIDGenerator:
    """An iterator that infinitely generates unique UUID4 identifiers."""

    __slots__ = ('limit', 'count')

    def __init__(self, limit: int):

        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.limit is not None and self.count >= self.limit:
            raise StopIteration

        self.count += 1

        return str(uuid.uuid4())




if __name__ == '__main__':

    id_generator = UniqueIDGenerator(limit=10)

    print("Generating unique identifiers...")

    for uid in id_generator:
        print(uid)
