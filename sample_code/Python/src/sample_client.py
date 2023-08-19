import socket

HOST = "127.0.0.1" # localhost
PORT = 1234        # pixelflut-port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    
    ## Commands available:
    ## - Get Help: HELP
    ## - Retrieve color value of pixel at coordinate (x|y): PX <x> <y>
    ## - Color the pixel at coordinate (x|y) in color c (format rrggbb): PX <x> <y> <c>
    ## - Get canvas size: SIZE
    ## - Set offset of width w and height h for the duration of the connection: OFFSET <w> <h>

    sock.sendall(b"OFFSET 20 20\n")
    sock.sendall(b"PX 5 5 FF0000\n")

    ## If you want to received messages, handling might look like this
    # data = sock.rcv(1024)
    # print(f"{data!r}")