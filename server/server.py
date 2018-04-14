from websocketserver import SimpleWebSocketServer, WebSocket
from MotorDriver import MotorDriver

motor = MotorDriver()

class Socket (WebSocket):
    def handleConnected(self):
        print('device connected')
        motor.motor_direction_set(0b1010)

    def handleMessage(self):
        # echo message back to client
        data = str(self.data)
        (left, right) = data.split(':')
        motor.motor_speed_set(int(left), int(right))


if __name__ == '__main__':
    server = SimpleWebSocketServer('', 8000, Socket)
    server.serveforever()