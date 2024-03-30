import pygame

pygame.init()

SCREEN_WIDTH = 800   #создаем переменные ширины и высоты окна
SCRIEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCRIEN_HEIGHT))  #создаем переменную экран

pygame.display.set_caption("Игра тир")  #придумываем название окна
icon = pygame.image.load("")  # добавляем иконку 

running = true

while running:
    pass

pygame.quit()