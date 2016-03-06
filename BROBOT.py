import pygame
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.output(23,GPIO.HIGH)
pygame.mixer.init()
pygame.mixer.music.load("sandstorm.wav")
while pygame.music.mixer.get_busy() == True:
  continue
GPIO.output(23,GPIO.LOW)
