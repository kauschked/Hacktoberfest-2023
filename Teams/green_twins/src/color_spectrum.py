import socket
import time

HOST = "127.0.0.1" # localhost
# HOST = "10.201.77.56" # localhost
PORT = 1234        # pixelflut-port

def get_draw_color_command(x,y,color):
    return f"PX {x} {y} {color}"

# def rgb(i):
#     r = i % 256
#     g = (i//256) % 256
#     b = (i//256**2) % 256
#     print(f"{r} {g} {b}")
#     return f"{format(r,'02X')}{format(g,'02X')}{format(b,'02X')}"

def rgb(i):
    red = 255
    green = 0
    blue = 0

    if i > 0 and i <= 255:
        red = 255
        green = i
        blue = 0
    elif i > 255 and i <= 255*2:
        red = 255*2 - i
        green = 255
        blue = 0
    elif i > 255*2 and i <= 255*3:
        red = 0
        green = 255
        blue = i - 255*2
    elif i > 255*3 and i <= 255*4:
        red = 0
        green = 255*4 - i
        blue = 255
    elif i > 255*4 and i <= 255*5:
        red = i - 255*4
        green = 0
        blue = 255
    elif i > 255*5 and i <= 255*6:
        red = 255
        green = i - 255*5
        blue = 255


    # print(f"{red} {green} {blue}")

    return f"{format(red,'02X')}{format(green,'02X')}{format(blue,'02X')}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    
    ## Commands available:
    ## - Get Help: HELP
    ## - Retrieve color value of pixel at coordinate (x|y): PX <x> <y>
    ## - Color the pixel at coordinate (x|y) in color c (format rrggbb): PX <x> <y> <c>
    ## - Get canvas size: SIZE
    ## - Set offset of width w and height h for the duration of the connection: OFFSET <w> <h>

    x_offset = 0
    y_offset = 0
    for x in range(320):
        # print(rgb(x))
        command = "\n".join([get_draw_color_command(x + x_offset,y+y_offset, rgb(x*4)) for y in range(180)])
        # print(command)
        msg = bytes(f"{command}\n", "UTF-8")
        sock.sendall(msg)
        time.sleep(0.001)

    ## If you want to received messages, handling might look like this
    # data = sock.rcv(1024)
    # print(f"{data!r}")
