from urllib.parse import urlparse, parse_qs
from metadata_store import load_metadata

def handle_download(handler):
    query = parse_qs(urlparse(handler.path).query)
    file_id = query.get('docid', [None])[0]

    if not file_id:
        handler.send_response(400)
        handler.end_headers()
        handler.wfile.write(b"Missing docid")
        return

    metadata = load_metadata(file_id)
    if not metadata:
        handler.send_response(404)
        handler.end_headers()
        handler.wfile.write(b"File not found")
        return

    path = f"uploads/{metadata['filename']}"
    handler.send_response(200)
    handler.send_header("Content-Type", metadata["content_type"])
    handler.send_header("Content-Length", str(metadata["size"]))
    handler.end_headers()
    
    import shutil
    with open(path, "rb") as f:
        shutil.copyfileobj(f, handler.wfile)
