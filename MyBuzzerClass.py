import machine
import utime


class MyBuzzer:
    def __init__(self, pin):
        self.LOUDNESS = 32000

        self.pin = machine.PWM(machine.Pin(pin))
        self.pin.freq(440)  # Default frequency
        self.pin.duty_u16(0)  # Default duty cycle

    def play(self):
        self.pin.duty_u16(self.LOUDNESS)

    def set_freq(self, frequency_percentage):
        # Adjust frequency based on percentage
        self.pin.freq(50 + frequency_percentage * 95)

    def stop(self):
        self.pin.duty_u16(0)  # Stop sound
