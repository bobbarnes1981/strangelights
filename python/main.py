import time
import board
import neopixel

pixel_pin = board.D18
num_letters = 26
num_pixels = 50

letters = {
    "A":  0,
    "B":  1,
    "C":  2,
    "D":  3,
    "E":  4,
    "F":  5,
    "G":  6,
    "H":  7,
    "Q":  8,
    "P":  9,
    "O": 10,
    "N": 11,
    "M": 12,
    "L": 13,
    "K": 14,
    "J": 15,
    "I": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 21,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}

def on(p):
    j = 0
    for i in range(num_pixels):
        j += 1
        if j >= num_letters:
            j -= num_letters
        p[i] = colours[j]
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
        p[i] = colours[j]
        p.show()
        print(i, colours[j])
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
        print(colours[letters[l]])
        p[letters[l]] = colours[letters[l]]
        flicker(p, 20, 0.01)
        flicker(p, 10, 0.02)
        flicker(p,  5, 0.04)
        off(p)

YELLOW = (255,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

colours = [
    YELLOW, # A
    BLUE,   # B
    RED,    # C
    GREEN,  # D
    BLUE,   # E
    YELLOW, # F
    RED,    # G
    GREEN,  # H
    RED,    # Q
    GREEN,  # P
    RED,    # O
    RED,    # N
    YELLOW, # M
    GREEN,  # L
    BLUE,   # K
    RED,    # J
    GREEN,  # I
    GREEN,  # R
    BLUE,   # S
    YELLOW, # T
    BLUE,   # U
    RED,    # V
    BLUE,   # W
    YELLOW, # X
    RED,    # Y
    RED,    # Z
]

order = neopixel.RGB

brightness = 0.2

pixels = neopixel.NeoPixel(
    pixel_pin,
    num_pixels,
    brightness=brightness,
    auto_write=False,
    pixel_order=order
)

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

pixels.brightness = brightness
for i in range(10):
    trail(pixels, 0.1)
    time.sleep(1)
    off(pixels)

#pixels.fill((0,0,0))
#pixels.show()
