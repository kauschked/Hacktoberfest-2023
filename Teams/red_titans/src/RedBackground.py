import socket

HOST = "127.0.0.1" # localhost
PORT = 1234        # pixelflut-port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    XMIN=641
    XMAX=1279
    YMIN=0
    YMAX=719
    for y in range(YMIN, YMAX+1):
      for x in range(XMIN, XMAX+1):
             msg = bytes(f"PX {x} {y} FF0000\n", "UTF-8")
             sock.sendall(msg)
