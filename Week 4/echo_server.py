# Week 4 - Python Echo Server
from os import geteuid
import socket
from sys import argv, exit
from time import sleep

finished = False  # Have we received finished signal
num_of_bytes = 1024  # No. of bytes to accept
quit_message = "n"  # Quit message to end program

# Create a TCP socket
print("Starting server...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def main():
    try:
        try:
            ip_address = argv[1]  # Set ip address to first argument
            port = int(argv[2])  # Set port address to second argument
        except ValueError:
            print()
            print("Incorrect value for the port number. Please try again.")
            ip_address = input("Input IP address to listen on: ")  # Ask user to input IP address
            port = int(input("Input port to bind to: "))  # Ask user to input port number
    except IndexError:
        try:
            print()
            print("Usage: echo_server.py <hostname> <port>. You need to specify both hostname and port number.")
            ip_address = input("Input IP address to listen on: ")  # Ask user to input IP address
            port = int(input("Input port to bind to: "))  # Ask user to input port number
        except ValueError:
            print()
            print("Incorrect value for the port number. Please try again.")
            ip_address = input("Input IP address to listen on: ")  # Ask user to input IP address
            port = int(input("Input port to bind to: "))  # Ask user to input port number

    try:
        sock.bind((ip_address, port))
        sock.listen(1)  # Listen for incoming connections and only accept the first one
        print("Server listening on", ip_address, "on port", port, "\n")
    except PermissionError:
        if port <= 1024 and geteuid() != 0:
            print()
            print("Please choose a port above 1024 or run as root.")
            reply = input("To choose different IP address/port combination press 'y', otherwise choose 'n' to exit. ")
            if reply == "y" or "Y":
                ip_address = input("\nInput IP address to listen on: ")  # Ask user to input IP address
                port = int(input("Input port to bind to: "))  # Ask user to input port number
            elif reply == "n" or "N":
                print("Quitting in five seconds")
                sleep(5)
            else:
                print("Option not recognized... ")

    # Accept connection from a client
    connection, client_address = sock.accept()
    print("Received a connection from ", client_address, "\n")

    global finished
    while not finished:
        data_in = connection.recv(num_of_bytes)
        message = data_in.decode()

        print("Received from client:", message)

        if message == quit_message:
            finished = True
            print()
            print("Client quit.")
            break
        else:
            data_out = message.encode()
            connection.send(data_out)

    # Shutdown and close the connection
    print("Closing the connection ...")
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()

    # Shutdown and close the socket
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("\nYou have pressed Ctrl + C. Exiting ...")
        exit(0)
