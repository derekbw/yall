import time
import pygame
import RPi.GPIO as io
io.setmode(io.BCM)

pir_pin = 18

io.setup(pir_pin, io.IN)
pygame.mixer.init()
pygame.mixer.music.load("nexstaryall.wav")
pygame.mixer.music.set_volume(1.0)

while True:
	if io.input(pir_pin):
		if pygame.mixer.music.get_busy() == False:
			pygame.mixer.music.play()		
			time.sleep(10)
	time.sleep(0.5)
