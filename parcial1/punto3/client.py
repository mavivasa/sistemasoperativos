import socket
import webbrowser

CL_FILE_NAME = "downloaded_home.html"
SERVER_PORT = 9609

def init_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
        c.connect(('localhost', SERVER_PORT))
        
        print("Connection Established")

        data = c.recv(4096)
        data = data.decode()

        pagina = open(CL_FILE_NAME, "a")
        pagina.write(data)

        c.close()

        webbrowser.open_new_tab(CL_FILE_NAME)

init_client()