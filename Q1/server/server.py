import socket
import sys
import pickle

def manage_client(server_socket):
    client_socket, client_address = server_socket.accept()
    print(f"Connected by {client_address}")
            
    try:
        pickled_file = client_socket.recv(4096)

        file_data = pickle.loads(pickled_file)
                
        print(f"File from user: {file_data}")

        with open('./receivedData/data.txt', 'w') as file:
            file.write(file_data)
    except socket.error as msg:
        print(f"Caught exception socket.error in Client socket : {msg}")
    except pickle.UnpicklingError as e:
        print("Error occurred while unpickling data:", e)
    finally:
        client_socket.close()
        print("Client socket closed\n")

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 3000)) # ((HOST, PORT))
    server_socket.listen(1)
    try:
        print("Server is listening for incoming connections...")

        while True:
            manage_client(server_socket)
    except socket.error as msg:
        print(f"Caught exception socket.error in Server socket : {msg}")
    finally:
        server_socket.close()
        print("Server socket closed\n")
        
if __name__ == "__main__":
    run_server()
