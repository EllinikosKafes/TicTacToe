# server.py
import socket
import json
import threading

# Keep track of connected clients
clients = []
board = [""] * 9
turn = 0  # 0 = player 1, 1 = player 2

lock = threading.Lock()

def broadcast(data):
    for c in clients:
        c.send(json.dumps(data).encode())

def handle_client(conn, player_id):
    global board, turn
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break

            msg = json.loads(data.decode())
            print("Message received from client\n",msg)

            if msg["type"] == "update":
                with lock:
                    board = msg["board"]
                    # Switch turn
                    turn = 1 if turn == 0 else 0
                    # Broadcast updated board + turn to both clients
                    broadcast({"type": "update", "board": board, "turn": turn})
        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"Player {player_id+1} disconnected")
    
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(2)
    print("Server running, waiting for players...")

    while len(clients) < 2:
        conn, addr = server.accept()
        clients.append(conn)
        player_id = len(clients)-1
        print(f"Player {player_id+1} connected: {addr}")
        # Send player_id to client (0 or 1)
        conn.send(str(player_id).encode())
        threading.Thread(target=handle_client, args=(conn, player_id), daemon=True).start()

    print("Two players connected. Game starts!")

    # Keep the server running so daemon threads don’t exit
    try:
        while True:
            pass  # idle loop, main thread stays alive
    except KeyboardInterrupt:
        print("\nServer shutting down.")
        for c in clients:
            c.close()
        server.close()


if __name__ == "__main__":
    main()
    