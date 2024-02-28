import marshal
import types
import pickle
import socket


# Example function to pickle
def multiply(n):
    return n * n

# Serialize the function's code object and arguments
def serialize_function(func, *args):
    func_code = func.__code__
    serialized_data = marshal.dumps((func_code, args))
    return serialized_data

def connect_to_worker(port, arg):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", port))

    try:
        serialized_data = serialize_function(multiply, arg)
        client_socket.sendall(serialized_data)

        data = client_socket.recv(1024) 
        print(f"Received data from worker at port {port}: {data.decode()}")
    except socket.error as msg:
        print(f"Caught exception socket.error in Server socket : {msg}")
    finally:
        client_socket.close()
        print("Server socket closed\n")

def run_client():
    args = [5, 7]
    ports = [3000, 3001]
    for (port, arg) in zip(ports, args):
        connect_to_worker(port, arg)

if __name__ == "__main__":
    run_client()

