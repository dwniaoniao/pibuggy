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

allPins = [in1, in2, in3, in4, ena, enb]
leftPins = [in3, in4]
rightPins = [in1, in2]
forwardPins = [in1, in3]
backwardPins = [in2, in4]
inPins = [in1, in2, in3, in4]
pwmPins = [ena, enb]

GPIO.setup(allPins, GPIO.OUT, initial = GPIO.LOW)
pena = GPIO.PWM(ena, 100)   # 100Hz
penb = GPIO.PWM(enb, 100)
pena.start(0)
penb.start(0)

def forword(speed, duration = 0):
    pena.ChangeDutyCycle(speed)
    penb.ChangeDutyCycle(speed)
    GPIO.output(forwardPins, GPIO.HIGH)
    GPIO.output(backwardPins, GPIO.LOW)
    if duration:
        sleep(duration)
        GPIO.output(allPins, GPIO.LOW)

def backward(speed, duration = 0):
    pena.ChangeDutyCycle(speed)
    penb.ChangeDutyCycle(speed)
    GPIO.output(forwardPins, GPIO.LOW)
    GPIO.output(backwardPins, GPIO.HIGH)
    if duration:
        sleep(duration)
        GPIO.output(allPins, GPIO.LOW)

def turnLeft(speed, duration = 0):
    pena.ChangeDutyCycle(speed)
    penb.ChangeDutyCycle(speed)
    GPIO.output([in1, in4], GPIO.HIGH)
    GPIO.output([in2, in3], GPIO.LOW)
    if duration:
        sleep(duration)
        GPIO.output(allPins, GPIO.LOW)

def turnRight(speed, duration = 0):
    pena.ChangeDutyCycle(speed)
    penb.ChangeDutyCycle(speed)
    GPIO.output([in1, in4], GPIO.LOW)
    GPIO.output([in2, in3], GPIO.HIGH)
    if duration:
        sleep(duration)
        GPIO.output(allPins, GPIO.LOW)

def stop():
    GPIO.output(allPins, GPIO.LOW)

if __name__ == "__main__":
    try:
        forword(30, 1)
        turnLeft(60, 0.5)
        forword(30, 1)
        turnRight(60,2)
    except KeyboardInterrupt:
        pass

    pena.stop()
    penb.stop()
    GPIO.cleanup()

