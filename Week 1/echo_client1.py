# Week 1 - Python Echo Client
import socket

finished = False  # Did the user choose to finish the program?
server = "127.0.0.1"
port = 7
num_of_bytes = 1024  # No. of bytes to accept

# Create a TCP socket
print("Starting client socket ...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the echo server
sock.connect((server, port))
print("Connected to", server, "on port ", port, "\n")

while not finished:
    # Request, encode and send message to the echo server
    message_out = input("Enter message: ")
    data_out = message_out.encode()
    sock.send(data_out)

    # Receive and print response from the echo server
    data_in = sock.recv(num_of_bytes)
    message = data_in.decode()

    # Check to see if input is 'n' to quit loop
    if message == "n":
        finished = True
        print("Data entry stopped.\n")
        break

    # Print decoded message from echo server
    print("Received from server:", message)

# Shutdown and close the socket
print("Closing the socket connection ...")
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print("Done!")
