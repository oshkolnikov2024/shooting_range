import pygame
import random

pygame.init()

SCREEN_WIDTH = 800   #создаем переменные ширины и высоты окна
SCRIEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCRIEN_HEIGHT))  #создаем переменную экран

pygame.display.set_caption("Игра тир")  #придумываем название окна
icon = pygame.image.load("img/icon.jpg")  # добавляем иконку
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")  # добавляем картинку цели
target_width = 80   #размеры цели
target_height = 80

target_x = random.randint (0,SCREEN_WIDTH-target_width)    #hfyljvyst координаты x,y для цели
target_y = random.randint (0,SCRIEN_HEIGHT-target_height)

color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

running = true

while running:
    pass

pygame.quit()