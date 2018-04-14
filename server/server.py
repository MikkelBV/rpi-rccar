from websocketserver import SimpleWebSocketServer, WebSocket
from MotorDriver import MotorDriver

motor = MotorDriver()

class Socket (WebSocket):
    def handleConnected(self):
        print('device connected')
        motor.motor_drive()

    def handleMessage(self):
        # echo message back to client
        data = str(self.data)
        (left, right) = data.split(':')
        motor.motor_speed_set(int(left), int(right))


def run(port = 8000):
    server = SimpleWebSocketServer('', port, Socket)
    print('Socket server ready on port ' + port)
    server.serveforever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port = int(argv[1]))
    else:
        run()