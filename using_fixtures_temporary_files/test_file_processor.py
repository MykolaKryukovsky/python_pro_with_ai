"""
Unit tests for the FileProcessor class.
"""
from .file_processor import FileProcessor


def test_file_write_read(tmpdir):
    """
    Test that data is correctly written to and read from a file.
    """
    file = tmpdir.join("file.txt")
    data = "Hello World!"

    FileProcessor.write_to_file(file, data)
    content = FileProcessor.read_from_file(file)

    assert content == data

def test_empty_string(tmpdir):
    """
    Test handling of large data strings (1MB).
    """
    file = tmpdir.join("large.txt")
    large_data = "A" * 10 ** 6

    FileProcessor.write_to_file(file, large_data)

    assert FileProcessor.read_from_file(file) == large_data

def test_overwrite_existing_file(tmpdir):
    """
    Test that writing to an existing file overwrites its content.
    """
    file = tmpdir.join("overwrite.txt")
    FileProcessor.write_to_file(file, "First version")
    FileProcessor.write_to_file(file, "Second version")

    assert FileProcessor.read_from_file(file) == "Second version"
