from rpi_board import RpiBoard
import time

hardware = RpiBoard()

brightness = 0.01
increasing_brightness = True

while True:
    print(brightness)
    hardware.set_pwm(18, brightness)

    if increasing_brightness:
        brightness += 0.01
        if brightness >= 1:
            increasing_brightness = False
    else:
        brightness -= 0.01
        if brightness <= 0:
            increasing_brightness = True

    time.sleep(0.1)
