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

    sock.sendall(b"SIZE\n")
    print(sock.recv(1024))
    
    sock.sendall(b"OFFSET 20 20\n")
    msg = bytes(f"PX 13 37 FF0000\n", "UTF-8")
    sock.sendall(msg)
    
    sock.sendall(b"PX 13 37\n")
    print(sock.recv(1024))

    ## If you want to received messages, handling might look like this
    # data = sock.rcv(1024)
    # print(f"{data!r}")
