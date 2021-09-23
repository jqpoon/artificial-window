from arduino_board import ArduinoBoard
import time

arduino = ArduinoBoard()

while True:

    arduino.gpio_on(13)

    time.sleep(1)

    arduino.gpio_off(13)

    time.sleep(1)

