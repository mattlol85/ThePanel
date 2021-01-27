import time
import RPi.GPIO as GPIO
from gpiozero import LED
from gpiozero import Button

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#GPIO.setup(2, GPIO.OUT)
#GPIO.output(2, GPIO.HIGH)

button = Button(2)

while True:
    if button.is_pressed:
        print("Button Is pressed")
    else:
        print("Button not pressed")