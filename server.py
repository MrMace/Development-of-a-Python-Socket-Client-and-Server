import socket

host = socket.gethostname()  
port = 9500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))
    s.listen()
    connection, addr = s.accept()
    with connection:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            connection.sendall(data)
