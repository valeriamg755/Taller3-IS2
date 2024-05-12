import socket
import threading

def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")

    while True:
        message = client_socket.recv(1024).decode("utf-8")
        if not message:
            print(f"[DISCONNECTED] {address} disconnected.")
            break
        
        print(f"[{address}] {message}")
        
        broadcast(message)

    client_socket.close()

def broadcast(message):
    for client in clients:
        client.send(message.encode("utf-8"))

HOST = 'localhost'
PORT = 2224

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen()

print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

clients = []

while True:
    client_socket, address = server_socket.accept()

    clients.append(client_socket)

    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
