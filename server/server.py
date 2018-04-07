from websocketserver import SimpleWebSocketServer, WebSocket


def print_to_pi(left, right):
    print('left: ' + left + ', right: ' + right)


class SimpleEcho(WebSocket):
    def handleMessage(self):
        # echo message back to client
        data = str(self.data)
        (left, right) = data.split(':')
        print_to_pi(left, right)


if __name__ == '__main__':
    server = SimpleWebSocketServer('', 8000, SimpleEcho)
    server.serveforever()