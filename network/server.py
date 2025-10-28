# network/server.py
import socket
import pickle

# Set up server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen(2)
print("🟢 Server started, waiting for 2 players...")

connections = []
addresses = []

while len(connections) < 2:
    conn, addr = server.accept()
    print(f"Player connected from {addr}")
    connections.append(conn)
    addresses.append(addr)

print("✅ Both players connected! Game starting...")

connections[0].send("ready".encode())
connections[1].send("ready".encode())

turn = 0  # 0 or 1 to indicate whose turn it is

while True:
    try:
        # Receive a move from current player
        data = connections[turn].recv(1024)
        if not data:
            break

        move = pickle.loads(data)
        print(f"Player {turn + 1} played {move}")

        # Send the move to the other player
        other = 1 - turn
        connections[other].send(pickle.dumps(move))

        # Switch turns
        turn = other

    except Exception as e:
        print("❌ Error:", e)
        break

for conn in connections:
    conn.close()

print("Server closed.")
