import socket
import sys
import numpy as np
from PIL import Image


HOST = "10.201.77.56" # localhost
PORT = 4321        # pixelflut-port

OFFSET_X=5
OFFSET_Y=365

CAT="images/cats.jpg"
THUG="images/thug.jpg"

def main():
    img = openImage(CAT)
    thug = openImage(THUG)
    # withThug = addThug(img, thug, (50,0))
    withThug = addThug(img, thug, (50,170))

    images = []

    for i in range(0, 170, 25):
        images.append(addThug(img, thug, (50,i)))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        
        fullSize = readSize(sock)
        width, height = fullSize
        offset = (OFFSET_X, OFFSET_Y)

        for im in images:
            writePx(offset, im, sock)

def addThug(img, thug, offset):
    img2 = np.copy(img)
    ox, oy = offset
    for iy, ix, _ in np.ndindex(thug.shape):
        color = thug[iy, ix]
        if color[0] > 200 and color[1] > 200 and color[2] > 200:
            continue
        img2[iy+oy, ix+ox] = thug[iy, ix]
    return img2
    

def openImage(path):
    image = Image.open(path)
    imgNumpy = np.asarray(image)
    return imgNumpy


def readSize(sock):
    msg = bytes(f"SIZE\n".encode("utf-8"))
    sock.sendall(msg)
    data = str(sock.recv(1024), "utf-8")
    splits = data.split()
    return (int(splits[1]), int(splits[2]))

def writePx(offset, canvas, sock):
    msg = ""
    for iy, ix, zz in np.ndindex(canvas.shape):
        c = colorStr(canvas[iy, ix])
        iy = iy + offset[1]
        ix = ix + offset[0]
        msg += writePxCmd(ix, iy, c)

    msg = bytes(msg.encode('utf-8'))
    sock.sendall(msg)    

def writePxCmd(x: int, y: int, color) -> str:
    return f"PX {x} {y} {color}\n"

def createColorGradient(size):
    width, height = size
    startColor = [255, 0, 0]  # Red
    endColor = [0, 0, 255]    # Blue
    canvas = createGradient(startColor, endColor, width, height)
    return canvas

def colorStr(color):
    r, g, b = color
    return '%02x%02x%02x' % (r, g, b)

def createGradient(startColor, endColor, width, height):
    start_rgb = np.array(startColor)
    end_rgb = np.array(endColor)
    gradient = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            factor = x / (width - 1)
            color = (1 - factor) * start_rgb + factor * end_rgb
            gradient[y, x, :] = color

    return gradient



if __name__ == '__main__':
    sys.exit(main())