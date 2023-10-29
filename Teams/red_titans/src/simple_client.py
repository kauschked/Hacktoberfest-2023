import socket
import random
import cv2
from PIL import Image

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("10.201.77.56", 4321))
#s.connect(("127.0.0.1", 5900))
s.connect(("127.0.0.1", 1234))


def pixel(x,y,r,g,b,a=255):
    if a == 255:
        s.send(f"PX {x} {y} {r:02x}{g:02x}{b:02x}\n".encode("utf-8"))
    else:
        s.send(f"PX {x} {y} {r:02x}{g:02x}{b:02x}{a:02x}\n".encode("utf-8"))

def line(x1,y1,x2,y2,r,g,b):
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    
    if dx == 0:
        rect(x1,y1,dy,1,r,g,b)
        return
    if dy == 0:
        rect(x1,y1,1,dx,r,g,b)
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

        pixel(x,y,r,g,b)

def rect(x,y,w,h,r,g,b):
  for i in range(x,x+w):
    for j in range(y,y+h):
      pixel(i,j,r,g,b)

def worm(x,y,n,r,g,b):
    while n:
        rx = random.randint(0,200)-100
        ry = random.randint(0,200)-100
        line(x, y, x + rx, y + ry, r, g, b)
        x += rx
        y += ry
        n -= 1

def blit(offsetx, offsety, image):
    for ix in range(0, image.width):
        for iy in range(0, image.height):
            r, g, b = image.getpixel((ix,iy))
            pixel(offsetx+ix, offsety + iy,r,g,b)

def clean(xmin, xmax, ymin, ymax):
    for ix in range(xmin, xmax+1):
        for iy in range(ymin, ymax+1):
            pixel(ix,iy,0,0,0)

def get_canvas_size():
    s.send(f"SIZE\n".encode("utf-8"))
    buf = ""
    while True:
        data = s.recv(1024)
        if not data:
            break
        buf += data.decode()
        if "\n" in buf:
            break
    data = buf.split(" ")
    return int(data[1]), int(data[2])


def get_help():
    s.send(f"HELP\n".encode("utf-8"))
    buf = ""
    while True:
        data = s.recv(1024)
        if not data:
            break
        buf += data.decode()
        if "\n" in buf:
            break
    return data


def set_offset(offset_x, offset_y):
    s.send(f"OFFSET {int(offset_x)} {int(offset_y)}\n".encode("utf-8"))


def random_movement(smallimg):
    start_x = 10
    start_y = 10
    # Set up the step value
    step = 100
    for i in range(5):
        # Calculate the new coordinates
        new_x = start_x + step * i
        new_y = start_y + step * i
        blit(new_x+100, new_y+100, smallimg)
        
        # attention to the offset
        clean(new_x+100, new_x+100 + smallimg.width, new_y+100, new_y+100+smallimg.height)

def move_image(img, offset_x, offset_y):
    blit(offset_x, offset_y, img)
    # attention to the offset

def convert_cv2_to_image(cv2_image):
    cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(cv2_image)
    return pil_image


import time
def run():
    #img = Image.open('src/rgb.png')
    img = Image.open('/src/deal-with-raccon.png')
    #blit(641,721,smallimg)

    print(f"Help: {get_help()}")

    width, height = get_canvas_size()
    print(f"XX size: {width}, {height}")


    img2 = cv2.imread('/src/deal-with-raccon.png')

    one_third_width = int(width / 3)
    one_third_heigth = int(height / 3)
    
    cv2_resized_img = cv2.resize(img2,(one_third_width,one_third_heigth))
    pil_image = convert_cv2_to_image(cv2_resized_img)

    # Get the bounding box
    bbox = pil_image.getbbox()
    # Extract x_min, y_min, x_max, and y_max
    x_min, y_min, x_max, y_max = bbox

    #resized_img = cv2.resize(img2, (1920 / 3, 1080 / 3))

    #random_movement(convert_cv2_to_image(resized_img))
    sleep_duration = 0.3

    for i in range(5):
        move_image(pil_image, 0,0)
        time.sleep(sleep_duration)
        clean(x_min, x_max,y_min, y_max)

        move_image(pil_image, one_third_width, 0)
        time.sleep(sleep_duration)
        clean(one_third_width+ x_min, one_third_width + x_max,y_min, y_max)
        
        move_image(pil_image, one_third_width*2, 0)
        time.sleep(sleep_duration)
        clean(one_third_width*2+ x_min, one_third_width*2+ x_max,y_min, y_max)
        
        move_image(pil_image, one_third_width*2, one_third_heigth)
        time.sleep(sleep_duration)
        clean(one_third_width*2+ x_min, one_third_width*2+ x_max, one_third_heigth, y_max+one_third_heigth)
        
        move_image(pil_image, one_third_width*2, one_third_heigth*2)
        time.sleep(sleep_duration)
        clean(one_third_width*2+ x_min, one_third_width*2+ x_max, one_third_heigth*2, y_max+one_third_heigth*2)
        
        move_image(pil_image, one_third_width*1, one_third_heigth*2)
        time.sleep(sleep_duration)
        clean(one_third_width*1+ x_min, one_third_width*1+ x_max, one_third_heigth*2, one_third_heigth*3)
        
        move_image(pil_image, 0, one_third_heigth*2)
        time.sleep(sleep_duration)
        clean(0, one_third_width, one_third_heigth*2, one_third_heigth*3)
        
        move_image(pil_image, 0, one_third_heigth*1)
        time.sleep(sleep_duration)
        clean(0, one_third_width, one_third_heigth*1, one_third_heigth*2)
    #move_image(0,0,convert_cv2_to_image(resized_img))





if __name__ == "__main__":
    clean(0,600,0,600)
    run()
    s.close()