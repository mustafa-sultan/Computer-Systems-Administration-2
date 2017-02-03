# Week 2 - Python Echo Client
import socket
from sys import argv, exit

finished = False
num_of_bytes = 1024  # No. of bytes to accept
quit_message = "n"  # Quit message to end program

# Create a TCP socket
print("Starting client...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    ip_address = input("Input IP address to connect to: ")  # Ask user to input IP address
    port = int(argv[1])  # Set port address to the first argument

    # Connect to the echo server
    sock.connect((ip_address, port))
    print("Connected to", ip_address, "on port", port, "\n")

    global finished
    while not finished:
        # Request and send message to the echo server
        message_out = input("Enter message: ")
        data_out = message_out.encode()
        sock.send(data_out)

        # Receive and print response from the echo server
        data_in = sock.recv(num_of_bytes)
        message = data_in.decode()

        # Check to see if input is 'n' to quit loop
        if message_out == quit_message:
            print("Data entry stopped.\n")
            finished = True
        else:
            # Print decoded message from echo server
            print("Received from server:", message)

    # Shutdown and close the socket
    print("Closing the socket connection ...")
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sock.send(quit_message.encode())
        print()
        print("\nYou have pressed Ctrl + C")
        exit()