import os
from utils import read_json, save_json, ensure_directory

META_PATH = 'uploads/metadata.json'

def save_metadata(file_id, metadata):
    """Saves file metadata against its unique file_id in the JSON store."""
    ensure_directory('uploads')
    if os.path.exists(META_PATH):
        data = read_json(META_PATH)
    else:
        data = {}
    data[file_id] = metadata
    save_json(META_PATH, data)

def load_metadata(file_id):
    if not os.path.exists(META_PATH):
        return None
    data = read_json(META_PATH)
    return data.get(file_id)
