"""
read the contents of a file in UTF-8 and output to stdout
"""

import sys


def read_file(filename: str) -> str:
    """
    Read the contents of a file in UTF-8 encoding and
    return the content as a string.

    Args:
        filename (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.

    Raises:
        FileNotFoundError: If the specified file does not exist.

    Examples:
        >>> read_file("path/to/file.txt")
        'File content'
    """
    with open(filename, mode="r", encoding="utf-8") as filestream:
        return filestream.read()


if __name__ == "__main__":  # pragma: no cover
    print(read_file(sys.argv[1]))
