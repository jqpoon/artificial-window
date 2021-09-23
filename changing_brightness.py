from arduino_board import ArduinoBoard
import time

arduino = ArduinoBoard()

brightness = 0.01
increasing_brightness = True

while True:
    print(brightness)
    arduino.set_pwm(11, brightness)

    if increasing_brightness:
        brightness += 0.01
        if brightness >= 1:
            increasing_brightness = False
    else:
        brightness -= 0.01
        if brightness <= 0:
            increasing_brightness = True

    time.sleep(0.1)