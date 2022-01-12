import socket
import sys


def http_client(hostname, port):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((hostname, port))

    request = "GET /basic.html HTTP/1.0\r\nHost:%s\r\n\r\n" % hostname
    clientSocket.send(request.encode())

    response = clientSocket.recv(4096)
    return response.decode()


def isValidUrl(url):
    return not url[0:5] == 'https'


def error(message):
    print(message, file=sys.stderr)
    sys.exit(1)


def getIPAddress(hostname):
    serverIpAddress = socket.gethostbyname(hostname)
    return serverIpAddress


def main():
    hostname = sys.argv[1]
    if not isValidUrl(hostname):
        error("Got https instead of http")

    targetPort = 80
    print(http_client(hostname, targetPort))


main()
