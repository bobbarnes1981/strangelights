import board
import neopixel
import time
from strange import Strange

brightness = 0.8

strange = Strange(
    board.D18,
    50,
    brightness,
    neopixel.RGB
)

while True:
    strange.show("HELP")

    strange.on()
    strange.flicker(2, 0.1)
    strange.flicker(5, 0.02)
    strange.flicker(2, 0.2)
    strange.off()

    strange.show("HELP")

    strange.on()
    strange.flicker(3, 0.1)
    strange.flicker(2, 0.2)
    strange.off()

    strange.show("RUN")

    strange.on()
    strange.flicker(2, 0.1)
    strange.flicker(5, 0.02)
    strange.flicker(2, 0.2)
    strange.off()

    strange.show("RUN")

    strange.on()
    strange.flicker(3, 0.1)
    strange.flicker(2, 0.2)
    strange.off()

    strange.on()
    strange.flicker(10, 0.15)
    strange.off()

    strange.brightness(brightness)
    for i in range(1):
        strange.trail(0.05)
        time.sleep(1)
        strange.off()

