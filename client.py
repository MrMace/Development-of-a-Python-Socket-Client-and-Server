import socket

host = socket.gethostname()
port = 9500
cts = True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        while cts == True:
            msg = input("Type what you would like to send ")

            s.sendall(msg.encode('ascii'))
            print("You: {}".format(msg))
            response = s.recv(1024)
            responseBack = response.decode('ascii')

            if responseBack == "Hi":
                print("Server: {}".format(responseBack))
            else:
                print("Server: {}".format(responseBack))

                cts = False
                s.close()
print("Connection Ended!")
