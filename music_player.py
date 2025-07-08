# pip install pygame

# music_player.py
# This script uses the Pygame library to play an audio file.
# It initializes the mixer, loads an audio file, and plays it until the playback is complete.

import pygame

pygame.mixer.pre_init(43000, -16, 2, 512)
pygame.mixer.init()

pygame.mixer.music.load("audio.wav")
# pygame.mixer.music.load("exp_025a.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass
pygame.mixer.quit()
