import socketserver


class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        self.data = self.request.recv(1024*100)
        print(f"{self.client_address}:\n\treceive data (size = {len(self.data)}): {self.data}")
        self.request.sendall(self.data)


if __name__ == "__main__":
    address = ("localhost", 9999)

    with socketserver.TCPServer(address, MyTCPHandler) as server:
        server.serve_forever()
