###################
# Driver Program for Raspberry Pi Lights/Switches/Buttons
#
# Pin Definitions
# GPIO18 - Digital Out NeoPixel W1228B
# GPIO2 - Button
# GPIO - Switch
# GPIO15 - Red Led
# GPIO14  - Green LED
###################
import time
import RPi.GPIO as GPIO
from gpiozero import LED
from gpiozero import Button
from signal import pause


#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#GPIO.setup(2, GPIO.OUT)
#GPIO.output(2, GPIO.HIGH)

button = Button(2)
redLed = PWMLED(15)
greenLed = LED(14)

while True:
    if button.is_pressed:
        greenLed.pulse()
        print("Button Is pressed")
        pause()
    else:
        print("Button not pressed")