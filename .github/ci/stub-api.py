import http.server
import sys
import time

port, status, body, log = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]


class Handler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        with open(log, "a") as f:
            f.write(f"POST {self.path} {self.headers.get('Authorization', '')}\n")
        if status == 0:
            time.sleep(60)
            return
        self.send_response(status)
        self.end_headers()
        self.wfile.write(body.encode())


http.server.HTTPServer(("127.0.0.1", port), Handler).serve_forever()
