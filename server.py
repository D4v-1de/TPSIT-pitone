import socket

HOST = "127.0.0.1"
PORT = 6767 # PORTA IN ASCOLTO

server_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM) #IPv4, TCP

socket = (HOST, PORT)
server_socket.bind(socket)
server_socket.listen() #socket in ascolto
conn, ip = server_socket.accept() #accetta la connessione

#abbiamo la connessione (conn) e l'indirizzo ip del client (ip)
bytes = conn.recv(20) #riceve un messaggio dal client (1024)--> bytes
print(bytes.decode())