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
    # TODO: fill in the hostname and port number
    # hostname = 'student00.ischool.illinois.edu'
    HOST = '192.168.0.101'
    PORT = 41030

    # A dummy message (in bytes) to test the code
    message = "Hello World"

    # TODO: convert the host name to the corresponding IP address
    # try:
    #     HOST = socket.gethostbyname(hostname)
    # except socket.error as e:
    #     print('Failed to convert hostname to IP address!')

    sin = (HOST, PORT)


    # TODO: create a datagram socket for TCP
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Failed to create socket.')
        sys.exit()


    # TODO: connect to the server
    try:
        connect_status = sock.connect(sin)
        if connect_status == -1:
            print('connect error')
    except socket.error as e:
        print('Failed to connect')
        sys.exit()

    # TODO: send the message to the server
    try:
        message = message.encode('utf-8')
        message_send_status = sock.send(message)
        if message_send_status == -1:
            print('message sent error')
    except socket.error as e:
        print('Failed to send message.')
        sys.exit()

    # TODO: receive the acknowledgement from the server
    try:
        ack = sock.recv(BUFFER)
    except socket.error as e:
        print('Failed to receive Acknowledgement.')
        sys.exit()

    # TODO: print the acknowledgement to the screen
    ack = int.from_bytes(ack, byteorder = 'big')
    print('Acknowledgement: {}'.format(ack))

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
