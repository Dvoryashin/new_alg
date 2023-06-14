import pygame
import time
import random

# Инициализируем импортированные модули
pygame.font.init()
pygame.init()

#Задаем переменные для цветов
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (9, 173, 6 )
blue = (50, 153, 213)
violet = (100, 0, 255)

# Ширина окна
dis_width = 600

# Высота окна
dis_height = 500

# Определяем главное окно
dis = pygame.display.set_mode((dis_width, dis_height))

# Задаём title
pygame.display.set_caption('Snake Game by Pythonist')

clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15

# pygame.font.Font('bionicle-training-card-font-2-4.ttf', 36)
game_over_font = pygame.font.Font("EightBits.ttf", 150)

score_font = pygame.font.Font("EightBits.ttf", 35)
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color, x, y, font_size):
    mesg = pygame.font.Font("EightBits.ttf", font_size).render(msg, True, color)
    dis.blit(mesg, [x, y])
 
def menu(length_of_snake):
    message(f'score: {length_of_snake - 1}', red, 10, 0, 35)
    message('|   q - quit', red, 120, 0, 35)
    message('space - pause', red, 270, 0, 35)
    message('r - restart', red, 440, 0, 35)

 
def gameLoop():
    game_over = False
    game_close = False
    pause = True
    direction = []

    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 + 40
    foody = random.randint(5, 43) * snake_block

    # Главный цикл игры
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            pygame.draw.line(dis, violet, [0, 45], [600, 45], 3)
            message("GAME OVER!", violet, 77, 100, 150)
            message('press "r" to restart ', violet, 150, 300, 50)
            menu(length_of_snake)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:

                # Если нажаты клавиши 
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_r:
                    return gameLoop()
                if event.key == pygame.K_LEFT:
                    if direction == 'right':
                        break
                    x1_change = -snake_block
                    y1_change = 0
                    direction = 'left'

                elif event.key == pygame.K_RIGHT:
                    if direction == 'left':
                        break
                    x1_change = snake_block
                    y1_change = 0
                    direction = 'right' 
            
                elif event.key == pygame.K_UP:
                    if direction == 'down':
                        break
                    y1_change = -snake_block
                    x1_change = 0
                    direction = 'up'
                elif event.key == pygame.K_DOWN:
                    if direction == 'up':
                        break
                    y1_change = snake_block
                    x1_change = 0
                    direction = 'down'
                if event.key == pygame.K_a:
                    if direction == 'right':
                        break
                    x1_change = -snake_block
                    y1_change = 0
                    direction = 'left'

                elif event.key == pygame.K_d:
                    if direction == 'left':
                        break
                    x1_change = snake_block
                    y1_change = 0
                    direction = 'right' 
            
                elif event.key == pygame.K_w:
                    if direction == 'down':
                        break
                    y1_change = -snake_block
                    x1_change = 0
                    direction = 'up'
                elif event.key == pygame.K_s:
                    if direction == 'up':
                        break
                    y1_change = snake_block
                    x1_change = 0
                    direction = 'down'
                elif event.key == pygame.K_SPACE:
                    pause = True
                    while pause == True:
                        time.sleep(0.1)
                        
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    pause = False
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 == 40:
            game_close = True
            continue

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        pygame.draw.line(dis, violet, [0, 45], [600, 45], 3)
        menu(length_of_snake)
    
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = random.randint(5, 43) * snake_block
            length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
gameLoop()