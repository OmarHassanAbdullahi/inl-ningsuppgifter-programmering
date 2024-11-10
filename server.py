import socket
import threading
# 
IP = "127.0.0.1"  
port = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, port))
server_socket.listen(5)  

# dict to store active clients in there usernmae 
clients = {}

def handle_client(client_socket):
    """
    This function listens for messages from the client and handles 
    sending them to other clients. If the client disconnects or sends an invalid message, 
    it will remove them from the list and close their connection.
    """
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                #the username of the client using the socket as the key
                user = clients.get(client_socket)
                print(f"Received message from {user}: {message}")
                 # Broadcast the message to all other clients
                broadcast_message(f"{user}: {message}", client_socket)
            else:
                #If not message is received, assume the client has left the chat
                raise Exception("Client left the chat")
        except Exception as e:
            print(f"Error: {e}")
            remove_client(client_socket)
            break

def broadcast_message(message, sender_socket=None):
    """
    This function sends the message to all connected clients, except the client 
    who sent the message (the sender). It allows all other clients to see the 
    messages sent by others.
    """
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                # Send the message to the client
                client_socket.send(message.encode('utf-8'))
            except:
                pass  # Ignore errors if a client is disconnected

def remove_client(client_socket):
    """
    This function removes a client from the 'clients' dictionary and closes their
    socket connection. it acts when a client disconnects from the server.
    """
    user = clients.pop(client_socket, None)# Remove the client from the dictionary
    if user:
        print(f"Removing user: {user} from clients")
    client_socket.close()

def accept_connections():
    """
    This function listens for new client connections. When a new 
    connection is made, it receives the client's username and starts 
    a new thread to handle the client. The server can handle multiple clients thanks to threading.
    """
    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address[0]}:{client_address[1]}")

        # Receive the username from the client
        user = client_socket.recv(1024).decode('utf-8')
        if user:
            clients[client_socket] = user
            print(f"User {user} has joined the chat.")
            broadcast_message(f"{user} has joined the chat!", client_socket)

            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

if __name__ == "__main__":
    print("Server is running...")
    accept_connections()  # Start accepting connections

	        
	
