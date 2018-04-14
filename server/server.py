from websocketserver import SimpleWebSocketServer, WebSocket
from MotorDriver import MotorDriver

motor = MotorDriver()

class Socket (WebSocket):
    def handleMessage(self):
        # echo message back to client
        data = str(self.data)
        (left, right) = data.split(':')
        print(data)
        motor.MotorSpeedSetAB(int(left), int(right))
        motor.MotorDirectionSet(0b1010)


if __name__ == '__main__':
    server = SimpleWebSocketServer('', 8000, Socket)
    server.serveforever()