from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from upload_handler import handle_upload
from download_handler import handle_download
from utils import ensure_directory

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        handle_upload(self)

    def do_GET(self):
        handle_download(self)

if __name__ == '__main__':
    ensure_directory('uploads')
    server = ThreadedHTTPServer(('0.0.0.0', 8000), RequestHandler)
    print("[+] Server running on http://0.0.0.0:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] Shutting down server gracefully...")
        server.server_close()
