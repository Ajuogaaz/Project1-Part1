import socket
import sys


def http_client():
    # serverport = 80
    return 0


def getIPAddress(hostname):
    serverIpAddress = socket.gethostbyname(hostname)
    return serverIpAddress


def main():
    hostname = sys.argv[1]
    print(getIPAddress(hostname))


main()
