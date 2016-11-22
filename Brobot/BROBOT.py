import pygame

pygame.mixer.init()
pygame.mixer.music.load("sandstorm.wav")
while pygame.music.mixer.get_busy() == True:
  continue
