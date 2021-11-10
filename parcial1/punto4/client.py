import socket
import asyncio
import os

SERVER_PORT = 9609

async def upload_file(file):
    socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketCliente.connect(('localhost', SERVER_PORT))
    try:
        socketCliente.send(file.encode())
    finally:
        socketCliente.close()


async def fileSelector():
    documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')

    os.chdir(documents)

    with os.scandir(os.getcwd()) as files:
        files = [file.name for file in files if file.is_file()]

    counter = 1

    for file in files:
        print(str(counter) + ". " + file)
        counter += 1
    
    inp = int(input("Enter the number of the file to be uploaded. "))

    return files[inp - 1]

async def folderSelector():
    documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')

    os.chdir(documents)

    with os.scandir(os.getcwd()) as files:
        files = [file.name for file in files if file.is_dir()]

    counter = 1

    for file in files:
        print(str(counter) + ". " + file)
        counter += 1
    
    inp = int(input("Enter the number of the folder to save the file."))

    return files[inp - 1]

async def download_file():
    socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketCliente.connect(('localhost', SERVER_PORT))
    try:
        data = socketCliente.recv(8192)
        folder = await folderSelector()
        data = data.decode()
        file = open(os.path.join(folder, "received"), "a")
        file.write(data)
    finally:
        socketCliente.close()




async def main():
    file = await fileSelector()
    await upload_file(file)
    await asyncio.sleep(1)
    await download_file()

asyncio.run(main())