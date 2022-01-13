import socket
import sys


def http_client(hostname, port, route):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((hostname, port))

    request = "GET " + route + " HTTP/1.0\r\nHost:%s\r\n\r\n" % hostname
    clientSocket.send(request.encode())

    response = clientSocket.recv(4096)
    return response.decode()


def isValidUrl(url):
    return url[0:5] != 'https' and url[0:4] == 'http'


def splitUrl(url):
    if not isValidUrl(url):
        error("Got https instead of http")

    urlWithoutHeader = url[7:]

    return splitUrlAndReconstruct(urlWithoutHeader)


def splitUrlAndReconstruct(url):

    url = url.split("/", 1)

    if len(url) == 1:
        return url[0], ""
    else:
        return url[0], "/"+url[1]

def getPort(url)

    url = url.split(":", 1)

    if len(url) == 1:
        return url[0], 80
    else:
        return url[0], int(url[1])


def error(message):
    print(message, file=sys.stderr)
    sys.exit(1)


def getIPAddress(hostname):
    serverIpAddress = socket.gethostbyname(hostname)
    return serverIpAddress


def main():
    parsedUrl, route = splitUrl(sys.argv[1])
    hostname, targetPort = getPort(parsedUrl[0])
    print(http_client(hostname, targetPort, route))


main()
