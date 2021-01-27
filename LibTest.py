import time
import board
import neopixel

# Data Pin for LED Ring
led_data_pin = board.D12
# Number of pixels
num_pixels = 12

# Set color order
ORDER = neopixel.GRB

# Instantiate the pixel strip object
pixels = neopixel.NeoPixel(
led_data_pin, num_pixels, brightness=0.2,
    auto_write=False,
    pixel_order=ORDER
)
counter = 0
while True:
    pixels.fill((255,0,0))
    pixels.show()
    time.sleep(1)
    print(counter+=1)
    
