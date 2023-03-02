import random
import threading
import multiprocessing
import time
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))
channel = connection.channel()
#channel_receive = connection.channel()


template = "Hello, {name}!"
names = ["Egor", "Sonya", "Nikita", "Andrey", "Konstantin"]


def send_message(exchange="", routing_key=""):
    n = 20

    for i in range(n):
        channel.basic_publish(exchange=exchange,
                                   routing_key=routing_key,
                                   body=bytes(f"{template.format(name=random.choice(names))}", encoding="utf-8"))

        time.sleep(0.2)


def receive_message(queue_name=""):
    n = 5

    #channel_receive.basic_consume(queue="test_queue",
    #                              auto_ack=True,
    #                              on_message_callback=message_received_callback)
    #
    #channel_receive.start_consuming()

    for *_, body in channel.consume(queue_name, auto_ack=True, inactivity_timeout=5):
        if body is not None:
            message_received_callback(None, None, None, body)
        else:
            print(f"{multiprocessing.current_process().name} stopped")
            break


def message_received_callback(ch, method, properties, body):
    print(f"{multiprocessing.current_process().name}. Received: {body.decode(encoding='utf-8')}")#\nFrom: {ch}\nMethod: {method}\nProperties: {properties}")


def create_queue(name):
    channel.queue_declare(queue=name)


def create_exchange(name):
    channel.exchange_declare(exchange=name)


def bind_exchange(exchange: str, queue: str, routing_key=""):
    channel.queue_bind(queue=queue, exchange=exchange, routing_key=routing_key)


if __name__ == "__main__":
    #create_queue("work_queue")
    #create_exchange("worker")
    #bind_exchange("worker", "work_queue", routing_key="work")

    sending_thread = threading.Thread(target=send_message, args=("worker", "work"), name="SendingThread")
    consumers_processes = [multiprocessing.Process(target=receive_message, args=("work_queue",),
                                                   name=f"consumer{i+1}_process") for i in range(3)]

    sending_thread.start()
    for process in consumers_processes:
        process.start()

    sending_thread.join()
    for process in consumers_processes:
        process.join()

    channel.close()
    connection.close()

