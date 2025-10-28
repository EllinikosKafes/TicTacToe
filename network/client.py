# network/client.py
import socket
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_and_rec(client):
    while True:
        move = input("Enter your move (e.g. 1,2 or 'exit'): ")

        if move.lower() == "exit":
            break

        # Send move
        client.send(pickle.dumps(move))

        # Wait for other player's move
        print("Waiting for the other player's move...")
        data = client.recv(1024)

        if not data:
            print("Disconnected.")
            break

        other_move = pickle.loads(data)
        print("Opponent played:", other_move)

    client.close()

def connect():
    global client
    client.connect(("127.0.0.1", 5555))
    print("🟢 Connected to server!")
    return True
    
def check_if_ready():
    try:
        if client.recv(1024).decode() == "ready":
            print("Got the ready sign, Returning TRUE")
            return True
    except Exception:
        print("Other player not connected yet")


    
