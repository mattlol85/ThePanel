import board
import neopixel
pixels = neopixel.NeoPixel(board.D12,12)

ORDER = neopixel.GRB
counter = 0
while True:
    pixels.fill((255,0,0))

    pixels.show()
    time.sleep(1)
    print(counter+1)
    