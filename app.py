import time
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging
 
logging.basicConfig(level=logging.INFO)

allocated_data = []

def allocate_memory(target_mb):
    global allocated_data
    mb_per_iteration = 10
    iterations = target_mb // mb_per_iteration

    for i in range(iterations):
        time.sleep(1)
        allocated_data.append(' ' * (10**6 * mb_per_iteration))
        logging.info(f"Allocated {mb_per_iteration * (i + 1)} MB of memory")
    return allocated_data

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Server is running\n")

def start_http_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    logging.info("Starting HTTP server on port 8080")
    httpd.serve_forever()

target_memory_mb = 800
allocate_memory(target_memory_mb)

time.sleep(10)

server_thread = threading.Thread(target=start_http_server)
server_thread.daemon = True
server_thread.start()

while True:
    time.sleep(1)