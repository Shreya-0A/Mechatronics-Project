import utime
from MyBuzzerClass import MyBuzzer
from MyServoClass import MyServo

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
