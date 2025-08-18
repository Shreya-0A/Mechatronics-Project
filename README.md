# Mechatronics-Project
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

class MyBuzzer:
    def __init__(self, pin):
        self.LOUDNESS = 62000
        
        self.pin = machine.PWM(machine.Pin(pin))
        self.pin.freq(440)  # Default frequency
        self.pin.duty_u16(0)  # Default duty cycle

    def play(self):
        self.pin.duty_u16(self.LOUDNESS)
    
    def set_freq(self, frequency_percentage):
        self.pin.freq(50 + frequency_percentage * 95)  # Adjust frequency based on percentage

    def stop(self):
        self.pin.duty_u16(0)  # Stop sound

servo = MyServo(15)
buzzer = MyBuzzer(11)

# Test buzzer

buzzer.set_freq(0)
buzzer.play()

for freq in range(0, 100):
    buzzer.set_freq(freq)
    utime.sleep(0.02)
for freq in range(100, 0, -1):
    buzzer.set_freq(freq)
    utime.sleep(0.02)

buzzer.stop()

# Test servo
servo.open()
utime.sleep(1)
servo.close()
