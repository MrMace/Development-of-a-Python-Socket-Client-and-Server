import socket

host = socket.gethostname()
port = 9500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen(2)
    connection, addr = s.accept()
    with connection:

        while True:
            data = connection.recv(1024)
            updatedData = data.decode('ascii')
            if updatedData == "Hello":
                respond = "Hi"
                print("Client: {}".format(updatedData))
                connection.send(respond.encode('ascii'))
                print("You: {}".format(respond))
            elif updatedData != "Hello" and updatedData != "":
                respond = "Goodbye"
                print("Client: {}".format(updatedData))
                connection.send(respond.encode('ascii'))
                print("You: {}".format(respond))

            else:
                print("Connection Ended!")

            if not data:
                break
            s.close()
