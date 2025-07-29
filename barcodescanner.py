from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8099

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/app/webapp", **kwargs)

with TCPServer(("", PORT), Handler) as httpd:
    print(f"[INFO] WebApp läuft unter Port {PORT}")
    httpd.serve_forever()