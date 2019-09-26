import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
middle = 7.2
top = 12.0

def setservo(theta):
    duty = ((0.01055555555 * theta) + 1.45)/20 * 100
    print('duty=')
    print(duty)
    servo.ChangeDutyCycle(duty)
    time.sleep(1.0)

try : 
    while 1:
        print("theta = ")
        a = input()
        setservo(a)
except KeyboardInterrupt:
    GPIO.cleanup()

