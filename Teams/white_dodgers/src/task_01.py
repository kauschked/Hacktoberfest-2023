import socket

HOST = "127.0.0.1" # localhost
PORT = 1234        # pixelflut-port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    x_max = 1920
    y_max = 1080

    x_width = int(x_max / 6)
    off_setx = x_width * 2
    y_width = int(y_max / 6)
    off_sety = y_width * 0
    offset = f"OFFSET {0} {0}\n"

    send_text = offset
    for x in range(x_width):
        for y in range(y_width):
            r = (off_setx+x) % 255
            g = (off_sety+y) % 255
            b = (off_setx+x) % 255
            send_text += f"PX {off_setx+x} {off_sety+y} "+ f'{r:02x}'+ f'{g:02x}'+ f'{b:02x}'+ '\n'

    send_text = bytes(send_text, "UTF-8")
    sock.sendall(send_text)