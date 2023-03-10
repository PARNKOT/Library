import pickle
import socket
import socketserver
import time
from multiprocessing import Process, current_process


ADDRESS = ("localhost", 9999)


def hello():
    print(f"{current_process().name}: Hello")


def send_func():
    print(f"{current_process().name}: started")
    print(f"{current_process().name}: waiting 1 second")
    time.sleep(1)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        print(f"{current_process().name}: sending {hello}")
        sock.sendall(pickle.dumps(hello))


class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        data = self.request.recv(1024*10)
        func = pickle.loads(data)
        print(f"{current_process().name}: executing {func}")
        func()


def receive_and_run_func():
    print(f"{current_process().name}: started")
    with socketserver.TCPServer(ADDRESS, MyTCPHandler) as server:
        server.serve_forever()


def decor(func):
    def wrapper(arg):
        func()

    wrapper.__name__ = func.__name__
    return wrapper


def func(arg: slice):
    print(type(arg))
    print(arg.start)


if __name__ == "__main__":
    func(slice(1, 3, 1))
    # server_process = Process(target=receive_and_run_func, name="ServerProcess")
    # client_process = Process(target=send_func, name="ClientProcess")
    #
    # server_process.start()
    # client_process.start()
    #
    # time.sleep(5)
    # server_process.terminate()
    # client_process.terminate()
