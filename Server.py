import socket
import datetime as dt
import threading
import Verify as av

# Select an appropriate port number. 
PORT = """Your Code here"""
# Set The Server's IP Address
SERVER_IP = """Your Code here"""
# Set up the Server's Address
ADDR = "(SERVER_IP, PORT)" """Your Code here"""
FORMAT = 'utf-8'

# Add code to initialize the socket
server = """Your Code here"""
# Write Code to bind Address to the server socket.
"""Your Code here"""

 # This function processes messages that are read through the Socket.
def clientHandler(conn, addr): 
    # Write Code that allows the Server to receive a connection code from an Agent. 
    """Your Code here"""

    # Write Code that allows the Server to check if the connection code received is valid. 
    """Your Code here"""

    # Write Code that allows the Server to retrieve a random secret question.
    """Your Code here"""

    # Write Code that allows the Server to send the random secret question to the Client.
    """Your Code here"""

    # Write Code that allows the Server to receive an answer from the Client.
    """Your Code here"""

    # Write Code that allows the Server to check if the answer received is correct.
    """Your Code here"""

    # Write Code that allows the Server to Send Welcome message to agent -> "Welcome Agent X" 
    """Your Code here"""

def runServer():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=clientHandler, args=(conn,addr) )
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}")

print("[STRTING] The Server is Starting...")
runServer()