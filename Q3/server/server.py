import socket
import threading

clients = []

def client_listener(connection, address):
    print(f"New connection from {address}")
    clients.append(connection)
    while True:
        try:
            message = connection.recv(1024).decode()
            if not message:
                break
            for client in clients:
                if client != connection:
                    client.send(message.encode())
        except Exception as e:
            print(f"Error: {e}")
            break

    clients.remove(connection)
    connection.close()

def run_server():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serversocket.bind(('', 5555))

    serversocket.listen(5)

    print("Server are listening...")
    
    while True:
        conn, addr = serversocket.accept()
        print(f"Client connected: {addr}")
        client_thread = threading.Thread(target=client_listener, args=(conn, addr))
        client_thread.start()
    
if __name__ == "__main__":
    run_server()
