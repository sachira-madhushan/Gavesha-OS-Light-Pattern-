from machine import Pin
import time

LEDS=[23,22,21,19,18,5,17,16,4,15]
for i in range(len(LEDS)):
	Pin(LEDS[i],Pin.OUT)

def OnOffLights(pin,mode):
	if mode:
		Pin(LEDS[pin]).on()
	else:
		Pin(LEDS[pin]).off()

def OrdianoPattern():
	while True:
		for i in range(10):
			j=0
			while(i>=j):
				OnOffLights(j,True)
				time.sleep(.10)
				j+=1

			time.sleep(.5)

			for z in range(j):
				OnOffLights(z,False)
			

		time.sleep(2)
		for i in range(10,-1,-1):
			x=9
			while (i<=x):
				#light on
				OnOffLights(x,True)
				time.sleep(.10)
				x-=1

			time.sleep(0.5)

			for z in range(i,10,1):			
				OnOffLights(z,False)

OrdianoPattern()