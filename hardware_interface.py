class HardwareInterface:
    def __init__(self):
        raise "Not implemented __init__"

    def gpio_on(self, pin_number):
        raise "Not implemented gpio_on"

    def gpio_off(self, pin_number):
        raise "Not implemented gpio_off"

    def set_pwm(self, pin_number, value):
        raise "Not implemented set_pwm"