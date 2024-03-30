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

target_x = random.randint (0,SCREEN_WIDTH-target_width)    #рандом координаты x,y для цели
target_y = random.randint (0,SCRIEN_HEIGHT-target_height)

color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

running = True

while running:
    screen.fill(color)  #заливка окна
    for event in pygame.event.get():  # обработка событий
        if event.type == pygame.QUIT: # проверка нажатия выхода
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # проверка нажатия мышки и вычисления попадания в цель
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)  # рандом координаты x,y для цели
                target_y = random.randint(0, SCRIEN_HEIGHT - target_height)
    screen.blit(target_img, dest=(target_x,target_y))  # отображение цели в координатах
    pygame.display.update()   # обновление окна

pygame.quit()