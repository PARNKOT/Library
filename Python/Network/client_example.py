import socket
import cv2
import base64
import numpy as np


def connect(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('localhost', 9999))
        sock.sendall(data)

        received = b''
        while True:
            recv = sock.recv(1024)
            if recv:
                received += recv #sock.recv(1024)
            else:
                break


    print(f"Sent size = {len(data)} bytes: {data}")
    print(f"Reсv size = {len(received)} bytes: {received}")
    print(data == received)

    return received


with open("images/image.png", "rb") as image:
    # encode
    bytes_array = base64.encodebytes(image.read())

    # send and receivev
    message = connect(bytes_array)

    # decode
    image_recv = base64.decodebytes(message)

    # converting from bytes to array[uint8]
    nparr = np.frombuffer(image_recv, np.uint8)

    # reading image from array[uint8]
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # show image
    cv2.imshow("", img_np)
    cv2.waitKey(0)
