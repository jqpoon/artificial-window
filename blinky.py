from rpi_board import RpiBoard
import time

rpi = RpiBoard()

while True:
    rpi.gpio_on(14)
    time.sleep(0.5)
    rpi.gpio_off(14)
    time.sleep(0.5)
