import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

in1 = 14
in2 = 15
in3 = 18
in4 = 23
ena = 24
enb = 25
pins = [in1, in2, in3, in4, ena, enb]
inpins = [in1, in2, in3, in4]
leftpins = [in3, in4]
rightpins = [in1, in2]
forwardpins = [in1, in3]
backwardpins = [in2, in4]

GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.LOW)

pena = GPIO.PWM(ena, 100)
penb = GPIO.PWM(enb, 100)
pena.start(30)
penb.start(30)

test = 1
try:
    while True:
        GPIO.output(forwardpins, GPIO.HIGH)
        GPIO.output(backwardpins, GPIO.LOW)
    pass
except KeyboardInterrupt:
    print('quit')
    pass

pena.stop()
penb.stop()
GPIO.cleanup()
