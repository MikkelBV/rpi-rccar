from websocketserver import SimpleWebSocketServer, WebSocket

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        print(self.data)
        #self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

if __name__ == '__main__':
    server = SimpleWebSocketServer('', 8000, SimpleEcho)
    server.serveforever()