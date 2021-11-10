import socket
import asyncio

HOST = '127.0.0.1'

SERVER_PORT = 9609

FILE_NAME = "home.html"

async def init_server(content):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, SERVER_PORT))

        s.listen(1)

        conn, addr = s.accept()

        conn.send(content.encode())

        print("File sent to client")

        conn.close()
    s.close()

async def main():

    file = open(FILE_NAME, "r")

    content = file.read()

    task1 = asyncio.create_task(init_server(content))

    await(task1)
    
asyncio.run(main())

