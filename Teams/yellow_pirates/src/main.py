
import socket

IP = "127.0.0.1"
PORT = 1234

OFFSET_X = 1
OFFSET_Y = 365

class Connection:
    def __init__(self, ip, port):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._ip = ip
        self._port = port

    def __enter__(self):
        self._socket.connect((self._ip, self._port))
        return self

    def __exit__(self, *args):
        if self._socket:
            self._socket.close()
            self._socket = None
        
    def get_canvas_size(self):
        self._socket.send(b"SIZE\n")

        buf = ""
        while True:
            data = self._socket.recv(1024)
            if not data:
                break
            buf += data.decode()
            if "\n" in buf:
                break
        data = buf.split(" ")
        return int(data[1]), int(data[2])

    def set_offset(self, offset_x, offset_y):
        cmd = f"OFFSET {int(offset_x)} {int(offset_y)}\n"
        self._socket.send(cmd.encode())
        
    def send_help(self):
        self._socket.send(b"HELP\n")
    
    def send_set_pixels(self, x, y, color):
        cmd = f"PX {x} {y} {color.upper()}\n"
        self._socket.send(cmd.encode())


RED = (0xFF, 0x00, 0x00)
GREEN = (0x00, 0xFF, 0x00)

def interpolate_colors(initial_color, target_color, steps):    
    # get the total difference between each color channel
    red_difference=target_color[0]-initial_color[0]
    green_difference=target_color[1]-initial_color[1]
    blue_difference=target_color[2]-initial_color[2]

    # divide the difference by the number of rows, so each color changes by this amount per row
    red_delta = red_difference/steps
    green_delta = green_difference/steps
    blue_delta = blue_difference/steps

    # display the color for each row
    interpolated = []
    for i in range(0, steps):
        # apply the delta to the red, green and blue channels
        interpolated.append((int(initial_color[0] + (red_delta * i)), 
                            int(initial_color[1] + (green_delta * i)),
                            int(initial_color[2] + (blue_delta * i))))
    
    return interpolated

def main():
    with Connection(IP, PORT) as conn:
        canvas_size = conn.get_canvas_size()
        segment_size = (int((canvas_size[0] - 7 )/ 6), int((canvas_size[1] - 7)/ 6))

        colors = interpolate_colors(RED, GREEN, segment_size[0])

        while True:
            color_itor = iter(colors)
            for x in range(segment_size[0]):
                color = next(color_itor)
                for y in range(segment_size[1]):
                    conn.send_set_pixels(x + OFFSET_X, y + OFFSET_Y, f"{color[0]:0{2}x}{color[1]:0{2}x}{color[2]:0{2}x}")



if __name__ == "__main__":
    main()