import neopixel
import random
import time
import logging

YELLOW = (255,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

logging.basicConfig(level=logging.DEBUG)

class Strange:
    letters = {
        # line 1
        "A":     2,
        "B":     3,
        "C":     4,
        "D":     5,
        "E":     6,
        "F":     7,
        "G":     8,
        "H":     9,
        # line 2
        "Q":    16,
        "P":    17,
        "O":    18,
        "N":    19,
        "M":    20,
        "L":    21,
        "K":    22,
        "J":    23,
        "I":    24,
        # line 3
        "R":    30,
        "S":    31,
        "T":    32,
        "U":    33,
        "V":    34,
        "W":    35,
        "X":    36,
        "Y":    37,
        "Z":    38,
    }
    colours = [
        YELLOW,
        RED,
        BLUE,
        GREEN,
    ]
    def __init__(self, pixel_pin: int, num_pixels: int, brightness: float, pixel_order: tuple[int, ...]) -> None:
        self.__logger = logging.getLogger("strange")
        self.__pixel_pin = pixel_pin
        self.__num_pixels = num_pixels
        self.__brightness = brightness
        self.__pixels = neopixel.NeoPixel(
            self.__pixel_pin,
            self.__num_pixels,
            brightness=self.__brightness,
            auto_write=False,
            pixel_order=pixel_order
        )
    def brightness(self, brightness: float) -> None:
        self.__pixels.brightness = brightness
    def on(self) -> None:
        j = 0
        for i in range(self.__num_pixels):
            j += 1
            if j >= len(self.letters):
                j -= len(self.letters)
            self.__pixels[i] = self.get_colour(j)
        self.__pixels.show()
    def off(self) -> None:
        for i in range(self.__num_pixels):
            self.__pixels[i] = (0,0,0)
        self.__pixels.show()
    def trail(self, speed) -> None:
        j = 0
        for i in range(self.__num_pixels):
            j += 1
            if j >= len(self.letters):
                j -= len(self.letters)
            self.__pixels[i] = self.get_colour(j)
            self.__pixels.show()
            self.__logger.info("%i %s", i, self.get_colour(j))
            time.sleep(speed)
    def flicker(self, count, speed) -> None:
        accuracy = [speed / 3, speed / 2]
        x = False
        for i in range(count*2):
            if x:
                self.__pixels.brightness = 0
            else:
                self.__pixels.brightness = self.__brightness
            self.__pixels.show()
            time.sleep(speed-random.choice(accuracy))
            x = not x
    def show(self, word) -> None:
        for l in word:
            self.__logger.info("%s %s %s", l, self.letters[l], self.get_colour(self.letters[l]))
            self.__pixels[self.letters[l]] = self.get_colour(self.letters[l])
            self.flicker(20, 0.01)
            self.flicker(10, 0.02)
            self.flicker( 5, 0.04)
            self.off()
    def get_colour(self, num: int) -> tuple[int]:
        return self.colours[num % len(self.colours)]

