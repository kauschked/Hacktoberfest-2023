import socket

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     sock.connect((HOST, PORT))
    
#     ## Commands available:
#     ## - Get Help: HELP
#     ## - Retrieve color value of pixel at coordinate (x|y): PX <x> <y>
#     ## - Color the pixel at coordinate (x|y) in color c (format rrggbb): PX <x> <y> <c>
#     ## - Get canvas size: SIZE
#     ## - Set offset of width w and height h for the duration of the connection: OFFSET <w> <h>


#     x_max = 1920;
#     sock.sendall(b"SIZE\n")
#     print(sock.recv(1024))
#     sock.sendall(b"HELP\n")
#     print(sock.recv(1024))
    
#     import socket

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


    x_max = 1920
    y_max = 1080


    x_width = int(x_max / 6)
    off_setx = x_width * 2
    y_width = int(y_max / 6)
    off_sety = y_width * 0
    offset = f"OFFSET {0} {0}\n"

    # sock.sendall(b"SIZE\n")
    # print(sock.recv(1024))
    # msg = bytes(f"PX 13 37 FF0000\n", "UTF-8")
    send_text = offset
    for x in range(x_width):
        for y in range(y_width):
            r = (off_setx+x) % 255
            g = (off_sety+y) % 255
            b = (off_setx+x) % 255
            send_text += f"PX {off_setx+x} {off_sety+y} "+ f'{r:02x}'+ f'{g:02x}'+ f'{b:02x}'+ '\n'
            # text = f"PX {y} {x} "+ f'{r:02x}'+ f'{g:02x}'+ f'{b:02x}'+ '\n'
            # print(text)
            # print(msg)
            # sock.sendall(msg)
            # print(text)
            # print(sock.recv(1024))

    send_text = bytes(send_text, "UTF-8")
    sock.sendall(send_text)

    ## If you want to received messages, handling might look like this
    # data = sock.rcv(1024)
    # print(f"{data!r}")
