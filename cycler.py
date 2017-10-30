
import board
import neopixel
import time


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.5)
pixels.fill((0,0,0))
pixels.show()

colorscheme2 = [ 
		(5,0,0), 
		(50,0,0), 
		(255,0,0), 
		]

class ColorCycler:
  def __init__(self, scheme, interval=0.01):
    self.scheme = scheme
    self.pix_index = 0
    self.interval = interval
    self.last_update = time.monotonic()

  def update(self):
    now = time.monotonic()
    if now - self.last_update > self.interval:
      pixels.fill((0,0,0))
      for i in range(len(self.scheme)):
	  pixels[(self.pix_index+i)%10] = self.scheme[i]
      self.pix_index += 1


cc = ColorCycler(colorscheme2)
while True:
    cc.update()
    time.sleep(0.001)
	
	
