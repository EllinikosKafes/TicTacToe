# network/client.py
import socket
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send(number):
    client.send(str(number)).encode()

def receive():
    return int(client.recv(1024).decode())


def connect():
    try:
        client.connect(('127.0.0.1', 5000))
        return True
    except:
        return False

def check_if_ready():
    data = client.recv(1024).decode()
    return data == "READY"