import socket
import threading

def receive_messages(client_socket):
    """Handles incoming messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("Disconnected from the server.")
            client_socket.close()
            break

def start_client():
    """Starts the client and connects to the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("Enter server IP (default: 127.0.0.1): ") or "127.0.0.1"
    client_socket.connect((server_ip, 5555))

    # Handle username input
    username = client_socket.recv(1024).decode()
    print(username, end="")
    client_socket.send(input().encode())

    # Start a thread for receiving messages
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    # Handle message sending
    while True:
        message = input()
        if message.lower() == "exit":
            break
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
