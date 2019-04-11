import time
import pygame
file=r'/Users/zifang/Music/网易云音乐/t.mp3'
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.music.stop()