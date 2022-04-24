# IS496: Computer Networks (Spring 2022)
# Programming Assignment 2 - Starter Code
# Name and Netid of each member:
# Member 1:
# Member 2:
# Member 3:

# Note:
# This starter code is optional. Feel free to develop your own solution to Part 1.
# The finished code for Part 1 can also be used for Part 2 of this assignment.


# Import any necessary libraries below
import socket
import sys


############## Beginning of Part 1 ##############
# TODO: define a buffer size for the message to be read from the TCP socket
BUFFER = 4096


def part1 ():
    print("********** PART 1 **********")
    # TODO: fill in the IP address of the host and the port number
    # HOST = socket.gethostbyname('student02.ischool.illinois.edu')
    HOST = '192.168.0.101'
    PORT = 41030
    sin = (HOST, PORT)

    # TODO: create a datagram socket for TCP
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Failed to create socket.')
        sys.exit()


    # Before Bind:
    # set socket options
    try:
        opt = 1
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, opt)
    except socket.error as e:
        print('Failed to set socket options')

    # TODO: Bind the socket to address
    try:
        sock.bind(sin)
    except socket.error as e:
        print('Failed to bind socket.')
        sys.exit()


    # TODO: start listening
    try:
        listen_status = sock.listen()
        if listen_status == -1:
            print('listen error')
    except socket.error as e:
        print('Failed to listen.')
        sys.exit()

    # TODO: accept the connection and record the address of the client socket
    try:
        new_sock, client_addr = sock.accept()
    except socket.error as e:
        print('Failed to accept.')
        sys.exit()

    # TODO: receive message from the client
    try:
        message = new_sock.recv(BUFFER)
    except socket.error as e:
        print('Failed to receive message.')
        sys.exit()

    # TODO: print the message to the screen
    message = message.decode('utf-8')
    print('Client Message: {}'.format(message))

    # TODO: send an acknowledgement (e.g., interger of 1) to the client
    ack = (1).to_bytes(2, 'big')
    try:
        ack_send_status = sock.send(ack)
        if ack_send_status == -1:
            print('acknowledgement sent error')
    except socket.error as e:
        print('Failed to send Acknowledgement.')
        sys.exit()

    # TODO: close the socket
    try:
        sock.close()
    except socket.error as e:
        print('Failed to close.')
        sys.exit()

############## End of Part 1 ##############




############## Beginning of Part 2 ##############

# main function for Part 2
def part2 ():
    pass


############## End of Part 2 ##############


if __name__ == '__main__':
# Your program will go with function part1() if there is no command line input.
# Otherwise, it will go with function part2() to handle the command line input
# as specified in the assignment instruction.
    if len(sys.argv) == 1:
        part1()
    else:
        part2()
