import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

target_width = 80   #размеры цели
target_height = 80

# Загрузка и инициализация первой цели
target_img = pygame.image.load("img/target.png")  # добавляем картинку цели

# Загрузка и инициализация второй цели
target_img_2 = pygame.image.load("img/target2.png")  # Предполагается другой файл для второй цели


# Инициализация координат для двух целей
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

target2_x = random.randint(0, SCREEN_WIDTH - target_width)
target2_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счётчики попаданий по целям
hits_target1 = 0
hits_target2 = 0

# Таймер для перемещения целей
MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 1000)  # перемещение каждую секунду

# Инициализируем шрифт
pygame.font.init()
default_font = pygame.font.Font(None, 36)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

running = True

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка события таймера для перемещения целей
        if event.type == MOVE_EVENT:
            # Перемещаем обе цели
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            target2_x = random.randint(0, SCREEN_WIDTH - target_width)
            target2_y = random.randint(0, SCREEN_HEIGHT - target_height)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка попадания по первой цели
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits_target1 += 1  # Увеличиваем счётчик попаданий
                print(f"Попадания по цели 1: {hits_target1}")
            # Проверка попадания по второй цели
            elif target2_x < mouse_x < target2_x + target_width and target2_y < mouse_y < target2_y + target_height:
                hits_target2 += 1  # Увеличиваем счётчик попаданий
                print(f"Попадания по цели 2: {hits_target2}")

    # Отображаем цели
    screen.blit(target_img, (target_x, target_y))
    screen.blit(target_img_2, (target2_x, target2_y))  # Для второй цели используем другую переменную

    # Отображение количества попаданий
    draw_text(f"Тукан: {hits_target1}", default_font, (0, 0, 0), screen, 5, 5)
    draw_text(f"Порося: {hits_target2}", default_font, (0, 0, 0), screen, 5, 40)

    pygame.display.update()

pygame.quit()