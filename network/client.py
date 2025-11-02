# client.py
import socket
import json

class LANClient:
    def __init__(self, host='localhost', port=5555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        # Receive player id (0 or 1)
        self.play_on_turn = int(self.client.recv(1024).decode())

    def update(self, board):
        # Send board to server
        message = json.dumps({"type": "update", "board": board})
        self.client.send(message.encode())
        print("Message sent to server\n",message)

    def listen(self,board):
        buffer = b""
        while True:
            chunk = self.client.recv(1024)
            if not chunk:
                return board, 0
            buffer += chunk
            try:
                msg = json.loads(buffer.decode())
                return msg["board"], msg["turn"]
            except json.JSONDecodeError:
                continue  # wait for more data

