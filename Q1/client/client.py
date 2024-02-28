import socket
import sys
import pickle

def pickle_file(file_path):
    try:
        with open(file_path, "r") as file:
            return pickle.dumps(file.read())
    except FileNotFoundError as e:
        print("File not found:", e)
    except IOError as e:
        print("Error occurred while reading file:", e)
    except pickle.PickleError as e:
        print("Error occurred while pickling object:", e)
    

def run_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 3000))
    try:
        file_path = input("Input your file path: ")
        pickled_file = pickle_file(file_path)
            
        client_socket.sendall(pickled_file)
        print("File sent successfully.")
    except socket.error as msg:
        print("Client socket error:", msg)
    finally:
        client_socket.close()
        print("Client socket closed")

if __name__ == "__main__":
    run_client()