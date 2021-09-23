from hardware_interface import HardwareInterface
import RPi.GPIO as GPIO
import time

class RpiBoard(HardwareInterface):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        self.pi_pwm = GPIO.PWM(18, 1000)
        self.pi_pwm.start(0)
        print("Init done!")

    def gpio_on(self, pin_number):
        GPIO.setup(pin_number, GPIO.OUT)
        GPIO.output(pin_number, GPIO.HIGH)

    def gpio_off(self, pin_number):
        GPIO.setup(pin_number, GPIO.OUT)
        GPIO.output(pin_number, GPIO.LOW)

    def set_pwm(self, pin_number, value):
        # Value must be between 0 and 1
        GPIO.setup(pin_number, GPIO.OUT)
        self.pi_pwm.ChangeDutyCycle(value * 100)
