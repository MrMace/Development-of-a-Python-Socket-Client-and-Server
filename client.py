import socket

host = socket.gethostname()  
port = 9500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))
    s.sendall(b"Hi")
    data = s.recv(1024)

print('Received', repr(data))
