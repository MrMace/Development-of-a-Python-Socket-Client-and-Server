# Development-of-a-Python-Socket-Client-and-Server


Begin by running the server.py first. 
```
$ python server.py
```
After it is up and running run the client.py in another terminal.
```
$ python client.py
```
The client.py will communicate with the server.py using websockets. This application it uses port: 9500. If the user will be requested to submit information to the server. The server will respond depending on what the user sends over. In this case if the client respond to the server 
```
You: "Hello"
```
the server will respond 
```
Server" "Hi"
```
If the client sends anything but "Hello" , Then the server would respond with a 
```
Server" "Goodbye"
```
It would also disconnect and the client and shut down the server (for the sake of the project and machine). 
