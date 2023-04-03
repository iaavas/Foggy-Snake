import os
import random
import pygame
author = 'Aavas Baral'


pygame.init()


game_bg = '#2C3A47'
snake_bg = '#fff200'

snake_text = '#FFA500'
snake_col = '#ff3838'
light_size = 40

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Foggy Snake By Aavash")

pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont('Consolas', 50)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(game_bg)
        text_screen("Foggy Snake", snake_text, 300, 250)
        text_screen("Developed by Aavash", snake_text, 200, 340)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    gameloop()
        pygame.display.update()
        clock.tick(30)


def gameloop():

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)

    score = 0
    init_velocity = 5
    snake_size = 10
    fps = 40
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            text_screen("Score: " + str(score), snake_text, 300, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
                score += 10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 5
                if score > int(highscore):
                    highscore = score
            gameWindow.fill(game_bg)

            # pygame.draw.rect(gameWindow, snake_bg,
            #                  pygame.Rect(snake_x-(light_size+score*1.2)/2, snake_y-(light_size+score*1.2)/2, light_size+score*1.2, light_size+score*1.2))
            pygame.draw.circle(gameWindow, snake_bg,
                               (snake_x, snake_y), light_size+score*0)

            plot_snake(gameWindow, snake_col, snk_list, snake_size)
            pygame.draw.rect(gameWindow, game_bg, [
                             food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


welcome()
