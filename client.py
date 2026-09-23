import socket

HOST = "127.0.0.1"
PORT = 6767 #PORTA A CUI CONNETTERSI

client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM) #IPv4, TCP

socket = (HOST, PORT)

#client_socket.bind(socket) non serve a nulla, il bind serve solo al server per mettersi in ascolto su una porta specifica. Il client si connette direttamente al server usando connect().

client_socket.connect(socket)
client_socket.sendall("Hello, server!".encode()) #invia un messaggio al server
