import socket
import asyncio
import ssl

file = open("result.txt", "w")

#Host and port, we use 443 as this API requires HTTPS support

hostname = "www.buda.com"
port = 443

#Creates an SSL context as instructed in: https://docs.python.org/3/library/ssl.html

context = ssl.create_default_context()

#Creates a request on demand given a request String

async def create_request(req):

    #Creates the client

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

        #Creates the connection

        client = context.wrap_socket(client, server_hostname = hostname)
        client.connect((hostname, port))

        #Sends the request String given as parameter

        client.send(req.encode())

        #We receive 5000 bytes for simplicity

        data = client.recv(5000).decode().split("\n")

        #We write the file with the data

        file.write(data.pop() + "\n")

async def main():

    #Request string to get list of markets

    markets = "GET /api/v2/markets HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"

    #Request string to get volume of given market: /api/v2/markets/{market-id}/volume
    #In this case BTC vs COP market volume

    COPMarket_volume = "GET /api/v2/markets/BTC-COP/volume HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"

    #Request string to get volume of given market: /api/v2/markets/{market-id}/ticker
    #In this case BTC vs COP market ticker

    COPMarket_ticker = "GET /api/v2/markets/BTC-COP/ticker HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"

    #Tuple holding awaitables created using the create_request function

    tasks = (create_request(markets), create_request(COPMarket_volume), create_request(COPMarket_ticker))

    #Gather the tasks and execute them in order: https://stackoverflow.com/questions/42231161/asyncio-gather-vs-asyncio-wait

    await asyncio.gather(*tasks)

    file.close()

#Run our asynchronous orchestra :)

asyncio.run(main())