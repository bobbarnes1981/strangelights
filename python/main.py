import time
import board
import neopixel

pixel_pin = board.D18
num_letters = 26
num_pixels = 50

letters = {
    "A":  2,
    "B":  3,
    "C":  4,
    "D":  5,
    "E":  6,
    "F":  7,
    "G":  8,
    "H":  9,

    "Q": 16,
    "P": 17,
    "O": 18,
    "N": 19,
    "M": 20,
    "L": 21,
    "K": 22,
    "J": 23,
    "I": 24,

    "R": 30,
    "S": 31,
    "T": 32,
    "U": 33,
    "V": 34,
    "W": 35,
    "X": 36,
    "Y": 37,
    "Z": 38,
}

def on(p):
    j = 0
    for i in range(num_pixels):
        j += 1
        if j >= num_letters:
            j -= num_letters
        p[i] = get_colour(j)
    p.show()

def off(p):
    for i in range(num_pixels):
        p[i] = (0,0,0)
    p.show()

def trail(p, speed):
    j = 0
    for i in range(num_pixels):
        j += 1
        if j >= num_letters:
            j -= num_letters
        p[i] = get_colour(j)
        p.show()
        print(i, get_colour(j))
        time.sleep(speed)

def flicker(p, count, speed):
    x = False
    for i in range(count*2):
        if x:
            p.brightness = 0
        else:
            p.brightness = brightness
        p.show()
        time.sleep(speed)
        x = not x

def show(p, word):
    for l in word:
        print(l)
        print(letters[l])
        print(get_colour(letters[l]))
        p[letters[l]] = get_colour(letters[l])
        flicker(p, 20, 0.01)
        flicker(p, 10, 0.02)
        flicker(p,  5, 0.04)
        off(p)

YELLOW = (255,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

colours = [
    YELLOW,
    BLUE,
    RED,
    GREEN,
]

def get_colour(num: int) -> tuple[int]:
    return colours[num % len(colours)]

order = neopixel.RGB

brightness = 0.6 #0.2

pixels = neopixel.NeoPixel(
    pixel_pin,
    num_pixels,
    brightness=brightness,
    auto_write=False,
    pixel_order=order
)

#show(pixels, "ABCDEFGH")
#show(pixels, "IJKLMNOPQ")
#show(pixels, "RSTUVWXYZ")

on(pixels)
flicker(pixels, 2, 0.1)
flicker(pixels, 5, 0.02)
flicker(pixels, 2, 0.2)
off(pixels)

show(pixels, "RUN")

on(pixels)
flicker(pixels, 3, 0.1)
flicker(pixels, 2, 0.2)
off(pixels)

show(pixels, "RUN")

on(pixels)
flicker(pixels, 10, 0.15)
off(pixels)

#pixels.brightness = brightness
#for i in range(10):
#    trail(pixels, 0.1)
#    time.sleep(1)
#    off(pixels)

#pixels.fill((0,0,0))
#pixels.show()

