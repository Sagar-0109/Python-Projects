import socket
import threading

class User:
    """Represents a chat user with a username and connection details."""
    def __init__(self, username, conn, addr):
        self.username = username
        self.conn = conn
        self.addr = addr

class Message:
    """Handles message formatting."""
    @staticmethod
    def format_message(username, message):
        return f"{username}: {message}"

class ChatRoom:
    """Manages connected users and message broadcasting."""
    def __init__(self):
        self.users = []  # List of connected users

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, message, sender):
        """Send message to all users except sender."""
        for user in self.users:
            if user != sender:
                try:
                    user.conn.sendall(message.encode())
                except:
                    user.conn.close()
                    self.remove_user(user)

# Initialize chat room
chat_room = ChatRoom()

def handle_client(conn, addr):
    """Handles client communication."""
    try:
        conn.send("Enter your username: ".encode())
        username = conn.recv(1024).decode()
        user = User(username, conn, addr)
        chat_room.add_user(user)
        
        print(f"{username} joined from {addr}")
        chat_room.broadcast(f"{username} has joined the chat!", user)

        while True:
            message = conn.recv(1024).decode()
            if not message or message.lower() == "exit":
                break

            formatted_message = Message.format_message(username, message)
            print(formatted_message)
            chat_room.broadcast(formatted_message, user)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print(f"{user.username} disconnected.")
        chat_room.broadcast(f"{user.username} has left the chat.", user)
        chat_room.remove_user(user)
        conn.close()

def start_server():
    """Starts the chat server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(5)
    print("Server is running on port 5555...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
