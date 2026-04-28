import os
import hashlib
import json


def ensure_directory(path):
    """Create the directory if it doesn't exist."""
    expanded_path = os.path.expanduser(path)
    if not os.path.exists(expanded_path):
        os.makedirs(expanded_path)
    return expanded_path


def md5_hash(data: bytes) -> str:
    """Compute MD5 hash of binary data."""
    return hashlib.md5(data).hexdigest()


def save_binary_file(path, data: bytes):
    """Save binary data to a file."""
    with open(path, "wb") as f:
        f.write(data)


def read_json(path):
    """Read JSON data from a file."""
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    """Write JSON data to a file."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
