# Week 2 - Python Echo Server
import socket
from sys import exit

finished = False  # Have we received finished signal
num_of_bytes = 1024  # No. of bytes to accept
quit_message = "n"  # Quit message to end program

# Create a TCP socket
print("Starting server...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def main():
    ip_address = input("Input IP address to listen on: ")  # Ask user to input IP address
    port = int(input("Input port to bind to: "))  # Ask user to input port number

    sock.bind((ip_address, port))
    sock.listen(1)  # Listen for incoming connections and only accept the first one
    print("Server listening on", ip_address, "on port", port, "\n")

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
        print("\nYou have pressed Ctrl + C")
    finally:
        print("Quitting Now. Bye.")
        exit(0)

