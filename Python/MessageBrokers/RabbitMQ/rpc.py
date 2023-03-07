import threading
import multiprocessing
import time
import uuid

import pika


#connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))
#channel = connection.channel()
#channel.queue_declare(queue="rpc_queue")


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def rpc_server():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))
    channel = connection.channel()
    channel.queue_declare(queue="rpc_queue")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="rpc_queue", on_message_callback=on_request)

    channel.start_consuming()


def on_request(ch, method, props, body):
    n = int.from_bytes(body, "big")

    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))

    ch.basic_ack(delivery_tag=method.delivery_tag)


class FibRpcClient():
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))
        self.channel = self.connection.channel()
        self.callback_queue = self.channel.queue_declare(queue='', exclusive=True).method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n: int):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        print(f"[rpc] Request {self.corr_id}: fib({n})")
        self.channel.basic_publish(
            exchange='',
            routing_key="rpc_queue",
            properties=pika.BasicProperties(reply_to=self.callback_queue, correlation_id=self.corr_id),
            body=n.to_bytes(4, byteorder="big")
        )

        self.connection.process_data_events(time_limit=None)
        return int(self.response)


def rpc_client():
    fib_rpc = FibRpcClient()

    response = fib_rpc.call(10)
    print(f"[rpc] Response {fib_rpc.corr_id}: {response}")


if __name__ == "__main__":
    server_process = multiprocessing.Process(target=rpc_server, name="ServerProcess")
    client_process = multiprocessing.Process(target=rpc_client, name="ClientProcess")

    server_process.start()
    client_process.start()

    time.sleep(5)
    server_process.terminate()
    client_process.terminate()