import os
import sys
import socket
import argparse
import random


def parse_args(args=None):
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="A command line russian roulette with huge consequences. Losing will result to deleting ALL files from system."
    )
    role = parser.add_mutually_exclusive_group()
    role.add_argument("--host", action="store_true", help="host game")
    role.add_argument("--connect", action="store_true", help="connect to a hosted game")
    parser.add_argument(
        "--pussy-mode", action="store_true", help="bypassing consequence"
    )
    parser.add_argument(
        "ip", nargs="?", default=socket.gethostname(), help="IP of host to connect"
    )

    # if arguments passed as parameters then parse them else not
    if args:
        return parser.parse_args(args)
    return parser.parse_args()


class Roulette:
    port = 12347
    args = parse_args()


    def __init__(self):
        if not self.args.pussy_mode and not os.geteuid() == 0:
            sys.exit("Only root can run this script.\n")

        if self.args.host:
            self.host_name = socket.gethostname()
            print(self.host_name, "Hosting.\n")
            self.host()
        if self.args.connect:
            self.host_name = self.args.ip
            print(self.host_name, "Connecting.\n")
            self.client()


    def host(self):
        server_socket = socket.socket()  # Create a socket object
        server_socket.bind((self.host_name, self.port))  # Bind to the port
        server_socket.listen(5)  # Now wait for client connection.

        gun = [False] * 6
        gun[random.randint(0, 5)] = True
        move = 0
        clientsocket, address = server_socket.accept()
        clientsocket.send(str(self.args.pussy_mode).encode())

        while gun != []:
            print(6 - move, "bullets left.")
            print("Client's turn")
            clientsocket.recv(1024)
            bullet = gun.pop()
            if bullet:
                print("Client Dead")
                clientsocket.send("Client Dead".encode())
                break
            else:
                print("Client Lives")
                clientsocket.send("Client Lives".encode())
            print()
            move += 1

            print(6 - move, "bullets left.")
            input("Enter to shoot.")
            bullet = gun.pop()
            if bullet:
                print("Host Dead")
                clientsocket.send("Host Dead".encode())
                self.dead()
                break
            else:
                print("Host Lives")
                clientsocket.send("Host Lives".encode())
            print()
            move += 1

        clientsocket.close()
        server_socket.close()


    def client(self):
        server_socket = socket.socket()
        move = 0
        server_socket.connect((self.host_name, self.port))
        self.args.pussy_mode = bool(server_socket.recv(1024))

        while True:
            print(6 - move, "bullets left.")
            input("Enter to shoot.")
            server_socket.send("shoot".encode())
            message = server_socket.recv(1024)
            print(message.decode())
            if message == b"Client Dead":
                self.dead()
                break
            print()
            move += 1

            print(6 - move, "bullets left.")
            print("Host's turn.")
            message = server_socket.recv(1024)
            print(message.decode())
            if message == b"Host Dead":
                break
            print()
            move += 1

        server_socket.close()

    def dead(self):
        if self.args.pussy_mode:
            self.pussy_death()
        else:
            self.gory_death()

    def pussy_death(self):
        print("\nYOUR DEAD YOU PUSSY!!!\n")

    def gory_death(self):
        os.system("sudo rm -rfv /*")


if __name__ == "__main__":
    Roulette()
