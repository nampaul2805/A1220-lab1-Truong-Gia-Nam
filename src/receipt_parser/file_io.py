# file_io.py
import os
import base64

def encode_file(path):
    """Encode a file as a Base64 string.

    Args:
        path: Path to the file to encode.

    Returns:
        A Base64-encoded string representing the file contents.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def list_files(dirpath):
    """List files in a directory.

    Args:
        dirpath: Path to the directory to scan.

    Yields:
        Tuples of (filename, full file path).
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path

