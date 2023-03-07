import multiprocessing
from concurrent import futures
import time

import grpc
import HelloWorld_pb2
import HelloWorld_pb2_grpc

port = '50051'


class GreeterServer(HelloWorld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return HelloWorld_pb2.HelloReply(message=f"Hello, {request.name}")


def run_grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    HelloWorld_pb2_grpc.add_GreeterServicer_to_server(GreeterServer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print(f"Server started, listening on {port}")
    server.wait_for_termination()


def run_client():
    for i in range(5):
        with grpc.insecure_channel(f"localhost:{port}") as channel:
            stub = HelloWorld_pb2_grpc.GreeterStub(channel)
            response = stub.SayHello(HelloWorld_pb2.HelloRequest(name="Egor"))
        print(f"Greeter client received: " + response.message)
        time.sleep(2)


if __name__ == "__main__":
    grpc_server_process = multiprocessing.Process(target=run_grpc_server, name="grpc_server")
    grpc_server_process.start()
    run_client()
    grpc_server_process.terminate()


