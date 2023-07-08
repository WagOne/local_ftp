import socket
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
import threading

authorizer = DummyAuthorizer()
authorizer.add_anonymous(".", perm="elradfmwMT")

handler = FTPHandler
handler.authorizer = authorizer

server = servers.FTPServer(("0.0.0.0", 21), handler)

ip_address = socket.gethostbyname(socket.gethostname())
print(f"FTP-сервер запущен. IP-адрес: {ip_address}")

def stop_ftp_server():
    input("Нажмите Enter для остановки FTP-сервера...")
    server.close_all()
    print("FTP-сервер остановлен.")

ftp_thread = threading.Thread(target=server.serve_forever)
ftp_thread.daemon = True
ftp_thread.start()

stop_ftp_server()

ftp_thread.join()
