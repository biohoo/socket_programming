'''
Tutorial from
https://www.youtube.com/watch?v=3QiPPX-KeSc

This will run on a local IP address

'''

import socket
import threading
import json

#   Put different messages in different threads
#   so program isn't waiting to finish receiving or sending

HEADER = 64 #   Bytes.
'''First message to a connection will always be 64 bytes.'''

PORT = 5050 #   Above port 4000 are inactive
SERVER = socket.gethostbyname(socket.gethostname()) #   This device
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


print(SERVER)

#   Create a socket of type INET and type streaming
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    '''Handles the individual connection
    between one client and one server.
    '''
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)   #   Blocking.  Will not pass until message received from socket.
        if msg_length:

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:   #   Disconnect message received
                connected = False

            try:                            #   Check to see if JSON received.
                json_object = json.loads(msg)
                print("[JSON SUCCESS] Printing JSON values...")
                for k, v in json_object.items():
                    print(k, v)
            except:
                print(f"{msg} is not a JSON object.")


            print(f"[{addr}] {msg}")
            conn.send("Msg received!".encode(FORMAT))
    conn.close()
    print(f"{addr} peaced out.")

def run_server():
    '''Starts the server and listens
    for multiple connections.'''

    server.listen()
    print(f"[LISTENING] server is listening on {server.getsockname()}")

    while True:
        conn, addr = server.accept()    #   This waits for a new connection.  Blocking call.
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")   #   Minus the thread that started this...

print("[STARTING] server is starting...")
run_server()