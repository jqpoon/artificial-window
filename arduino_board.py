import pyfirmata
from hardware_interface import HardwareInterface

class ArduinoBoard(HardwareInterface):
    def __init__(self):
        self.board = pyfirmata.Arduino('/dev/cu.usbmodem1301')
        it = pyfirmata.util.Iterator(self.board)
        it.start()
        print("Init done!")

    def gpio_on(self, pin_number):
        self.board.digital[pin_number].write(1)

    def gpio_off(self, pin_number):
        self.board.digital[pin_number].write(0)

    def set_pwm(self, pin_number, value):
        led = self.board.digital[pin_number]
        led.mode = pyfirmata.PWM
        led.write(value)