'''
Client-Server model

client - a device, computer, network, internet of things
server - central processing unit. Triages connections
    Example: instead of two computers directly communicating
    with one another, connecting through a Server as an intermediary
    will properly interpret requests and states.  This normalizes security.


Can run a server on a public OR local IP address...


Modem to internet
    1 public IP address



router to devices, allowing for modem connection
    local IP address - 192.168.1.xxx - IPv4/6
    per device


'''

import socket
import json

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    '''
    Sends a string (encoded into bytes) for submission to a server.

    :msg string
    '''
    message = msg.encode(FORMAT)    # Into bytes
    '''The first message sent should be the length of the message
    that is about to be sent.'''

    msg_length = len(message)
    print(f'message length: {msg_length}')
    send_length = str(msg_length).encode(FORMAT)

    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))



send(json.dumps({'hello':'there', 'how':234, 'are':False, 'You':23423423}))
send('Hello world')
send('My wife is driving me crazy')
send(DISCONNECT_MESSAGE)