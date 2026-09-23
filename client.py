import socket

HOST = "127.0.0.1"
PORT = 6767 #PORTA A CUI CONNETTERSI

client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM) #IPv4, TCP

socket = (HOST, PORT)

client_socket.bind(socket)






