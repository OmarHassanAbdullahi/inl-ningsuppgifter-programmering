import socket
import threading

def menu(): 
    """
    This function displays the menu options to the user.
    The user can choose to join the chat, leave the server, or exit the program.
    """
    print("1. join the chat")
    print("q. leave the chat")
    print("2.Exit the program")



def handle_chat(client_socket): 
    """
    This function allows the user to send messages to the chat.
    It continuously takes input from the user, sends the message to the server,
    and handles the case when the user types 'q' to leave the chat.
    """


       
    while True:
        message = input("You: ")

        # If user types 'q', leave the chat
        if message.lower() == "q":
            print("Leaving the chat...")
            client_socket.send("leave".encode('utf-8'))
            break
        else:
            # Send the message to the server
            client_socket.send(message.encode('utf-8'))

def receive_messages(client_socket):
    """
    This function listens for incoming messages from the server and prints them to the console.
    It runs in a separate thread so that the client can receive messages while typing.
    """
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
            else:
                break
        except:
            break

def client_program():
    """
    This function connects the client to the server, displays the menu for user choices,
    and handles joining the chat, leaving the server, and exiting the program.
    It starts separate threads to receive messages and allow the user to chat.
    """
    IP = "127.0.0.1" # ip adress (localhost)
    port = 1234 # the port the server is listening on 

#creating client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((IP, port))
        print("Connected to server.")
        
        while True:
            menu()

            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter your username: ")
                client_socket.send(username.encode('utf-8'))
                print(f"Joining the chat as {username}...")

                # Start a separate thread to listen for incoming messages
                receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
                receive_thread.start()

                # Start chatting
                handle_chat(client_socket)

            elif choice == "q":
                print("Disconnecting from the server...")
                client_socket.send("bye bye".encode('utf-8'))
                break  # Exit the program

            elif choice == "2":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. try again.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    client_program()	