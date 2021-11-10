import socket
import asyncio

SERVER_PORT = 9609

async def send_file(file):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind(('localhost', SERVER_PORT))
        s.listen(1)

        while True:
            conn, addr = s.accept()
            try:
                f = open(file, 'rb')
                content = f.read()
                conn.sendall(content)
                f.close()
                break
            finally:
                conn.close()


async def receive_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind(('localhost', SERVER_PORT))
        s.listen(1)

        while True:
            conn, addr = s.accept()

            try:
                data = conn.recv(8192)
                msg = data.decode()

            finally:
                conn.close()

            return msg


async def main():

    received_file = await receive_file()
    print("A file has been received: " + received_file)
    await send_file(receive_file)


asyncio.run(main())