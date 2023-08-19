import os, socket, signal
from threading import Thread

# This server starts up at localhost:1234 and prints any message send there. You can use it to dry-test your clients

HOST = "127.0.0.1" # Localhost
PORT = 1234 # Port (same as Pixelflut port)

class ServerThread(Thread):
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1024)
                    print(f"{data!r}")

pid = os.getpid()
server = ServerThread()
server.start()
input(f"Debugging server is listening at '{HOST}:{PORT}', press any key to quit...\n\n")
os.kill(pid, signal.SIGTERM)
