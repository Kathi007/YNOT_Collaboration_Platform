import socket
import sys

# Create a TCP/IPv4 socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_port = ('localhost', 54321) #Tuple with str & int
print('starting up on {} port {}'.format(*server_port))
sock.bind(server_port)

# Listen for incoming connections
sock.listen(1) #Only 1 connection at a time

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive 16 byte from client
        # If bytes are received, send back immediatelly and recieve next bits
        # If not, break connection & listen for new one
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
