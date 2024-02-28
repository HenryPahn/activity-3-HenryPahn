import marshal
import types
import pickle
import socket



# Deserialize and reconstruct the function
def deserialize_function(serialized_data):
    func_code, args = marshal.loads(serialized_data)
    reconstructed_func = types.FunctionType(func_code, globals(), "custom_function")
    return reconstructed_func(*args)

def run_server():
    # Server-side (where the function is defined)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 3000))
    server_socket.listen(5)

    try:
        print("Server is listening for incoming connections...")
        
        while True:
            connection_socket, address = server_socket.accept()
            print(f"Connected by {address}")

            try:
                # Serialize the function and its arguments
                data = connection_socket.recv(1024)

                result = deserialize_function(data)
                print(f"Result: {result}") 
                
                connection_socket.sendall(str(result).encode())
            finally:
                connection_socket.close()
                print("Connection closed\n")
    except socket.error as msg:
        print(f"Caught exception socket.error in Server socket : {msg}")
    finally:
        server_socket.close()
        print("Server socket closed\n")

if __name__ == "__main__":
    run_server()
