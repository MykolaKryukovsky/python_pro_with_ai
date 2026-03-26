"""Module for reading files in reverse order line by line."""
import os


class ReverseLineReader:
    """An iterator that reads a file from the end to the beginning."""

    __slots__ = ('file_path', 'buffer_size', 'file', 'position', 'buffer')

    def __init__(self, file_path: str, buffer_size: int = 4096):
        self.file_path = file_path
        self.buffer_size = buffer_size
        self.file = None
        self.position = 0
        self.buffer = b''

    def __enter__(self):
        self.file = open(self.file_path, 'rb')
        self.file.seek(0, os.SEEK_END)
        self.position = self.file.tell()

        if self.position > 0:
            self.file.seek(self.position - 1)
            if self.file.read(1) == b'\n':
                self.position -= 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        if self.file is None:
            raise RuntimeError("Use the iterator inside a 'with' block")

        while self.position > 0 or self.buffer:
            newline_index = self.buffer.rfind(b'\n')

            if newline_index != -1:
                current_line = self.buffer[newline_index + 1:]
                self.buffer = self.buffer[:newline_index]
                return current_line.decode('utf-8')

            if self.position > 0:
                read_size = min(self.position, self.buffer_size)
                self.position -= read_size
                self.file.seek(self.position)
                chunk = self.file.read(read_size)
                self.buffer = chunk + self.buffer
            else:
                result = self.buffer.decode('utf-8')
                self.buffer = b''
                return result

        raise StopIteration


if __name__ == '__main__':

    try:
        with ReverseLineReader('file123.txt', 4096) as reader:
            # Safe manual reading
            print(next(reader, "End of file"))
            print(next(reader, "End of file"))
            print(next(reader, "End of file"))

            for line in reader:
                print(line)
    except FileNotFoundError:
        print("Error: The file 'file123.txt' was not found.")
