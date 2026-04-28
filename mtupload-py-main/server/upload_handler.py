import uuid
from utils import md5_hash, save_binary_file
from metadata_store import save_metadata

def handle_upload(handler):
    if 'Content-Length' not in handler.headers:
        handler.send_response(411)
        handler.end_headers()
        handler.wfile.write(b"Length Required")
        return
        
    content_length = int(handler.headers['Content-Length'])
    content_type = handler.headers.get('Content-Type', 'application/octet-stream')
    raw_data = handler.rfile.read(content_length)

    file_id = str(uuid.uuid4())
    filename = f"{file_id}.bin"
    path = f"uploads/{filename}"

    save_binary_file(path, raw_data)
    metadata = {
        "filename": filename,
        "content_type": content_type,
        "size": len(raw_data),
        "md5": md5_hash(raw_data)
    }
    save_metadata(file_id, metadata)

    handler.send_response(200)
    handler.end_headers()
    handler.wfile.write(file_id.encode())
