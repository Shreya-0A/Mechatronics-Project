import machine
import utime


def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class MyServo:
    def __init__(self, pin):
        self.pin = machine.PWM(machine.Pin(pin))
        self.pin.freq(50)

    def write(self, angle):
        pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5)
        duty = int(interval_mapping(pulse_width, 0, 20, 0, 65535))
        self.pin.duty_u16(duty)

    def open(self):
        self.write(0)

    def close(self):
        self.write(90)
