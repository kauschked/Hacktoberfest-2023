import socket
import random

class PixelClass:
    def __init__(self,xmin,xmax,ymin,ymax) -> None:
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(("127.0.0.0", 1234))

    def pixel(self, x,y,r,g,b, a=255):
        if a == 255:
            self.s.send(f"PX {x} {y} {r:02x}{g:02x}{b:02x}\n".encode("utf-8"))
        else:
            self.s.send(f"PX {x} {y} {r:02x}{g:02x}{b:02x}{a:02x}\n".encode("utf-8"))

    def line(self, x1,y1,x2,y2,r,g,b):
        x,y = x1,y1
        dx = abs(x2 - x1)
        dy = abs(y2 -y1)
        
        if dx == 0:
            self.rect(x1,y1,dy,1,r,g,b)
            return
        if dy == 0:
            self.rect(x1,y1,1,dx,r,g,b)
            return
        
        gradient = dy/float(dx)

        if gradient > 1:
            dx, dy = dy, dx
            x, y = y, x
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        p = 2*dy - dx    

        for k in range(2, dx + 2):
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p = p + 2 * (dy - dx)
            else:
                p = p + 2 * dy

            x = x + 1 if x < x2 else x - 1

            self.pixel(x,y,r,g,b)

    def rect(self,x,y,w,h,r,g,b):
        for i in range(x,x+w):
            for j in range(y,y+h):
                self.pixel(i,j,r,g,b)

    def worm(self,x,y,n,r,g,b):
        while n:
            rx = random.randint(0,200)-100
            ry = random.randint(0,200)-100
            self.line(x, y, x + rx, y + ry, r, g, b)
            x += rx
            y += ry
            n -= 1

    def blit(self, x, y, image):
        for ix in range(0, image.width):
            for iy in range(0, image.height):
                r, g, b = image.getpixel((ix,iy))
                self.pixel(ix,iy,r,g,b)

    def clean(self):
        for ix in range(self.xmin, self.xmax+1):
            for iy in range(self.ymin, self.ymax+1):
                self.pixel(ix,iy,0,0,0)

