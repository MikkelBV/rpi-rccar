from http.server import BaseHTTPRequestHandler, HTTPServer
from server.MotorDriver import MotorDriver

class Server (BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        path = self.path;
        motor = MotorDriver()

        if path == '/drive':
            motor.motor_drive()
        elif path == '/reverse':
            motor.motor_reverse()

        self._set_headers()
        self.wfile.write((b'{}'))

    def do_HEAD(self):
        self._set_headers()

        
def run(port = 8081):
    server_address = ('', port)
    server = HTTPServer(server_address, Server)
    print('Car HTTP server ready on port ' + str(port))
    server.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port = int(argv[1]))
    else:
        run()
