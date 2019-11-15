import pygame as pg
import random
import sys

#   Main constants of the game

size = width, height = 500, 500
border_size = 10
color = 180, 212, 101
border_color = 99, 136, 64
size_rec = 25

#   Game functions of its rules

def rand_color(count):
    return random.randint(count, 255), random.randint(count, 255), random.randint(count, 255)

def random_position():
    x, y = (random.randint(2, width // size_rec) - 1) * size_rec, (random.randint(2, height // size_rec) - 1) * size_rec
    if x >= width - size_rec:
        x = width - 2 * size_rec
    if y >= height - size_rec:
        y = height - 2 * size_rec
    return x, y

def create_border(game_surface):
    for i in range(height):
        pg.draw.rect(game_surface, border_color, (0, i, size_rec, size_rec), 0)
        pg.draw.rect(game_surface, border_color, (width - size_rec, i, size_rec, size_rec), 0)
    for i in range(width):
        pg.draw.rect(game_surface, border_color, (i, 0, size_rec, size_rec), 0)
        pg.draw.rect(game_surface, border_color, (i, height - size_rec, size_rec, size_rec), 0)

#   Snake's food as an object

class Food(object):
    def __init__(self, x_pos_food = None, y_pos_food = None, food_color = None):
        if x_pos_food is None:
            x_pos_food, y_pos_food = random_position()
            food_color = (215, 54, 48)
        self.x_pos_food, self.y_pos_food, self.color = x_pos_food, y_pos_food, food_color

    def is_eaten(self, x, y):
        if x == self.x_pos_food and y == self.y_pos_food:
            self.x_pos_food, self.y_pos_food = random_position()

    def draw_food(self, game_surface):
        pg.draw.rect(game_surface, self.color, (self.x_pos_food, self.y_pos_food, size_rec, size_rec), 0)

#   Functions of menu buttons
#   Main game (Snake)

def startGame(screen):
    pg.display.set_caption('Snake')
    meal = Food()
    gameover = False
    while not gameover:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = True
        screen.fill(color)
        create_border(screen)
        meal.draw_food(screen)
        pg.display.flip()
        pg.time.wait(10)
    sys.exit()

#   For sec button

def about_us(screen):
    pg.display.set_caption('About Us')
    screen.fill(color)
    create_border(screen)
    data = ['Developed by:', 'Fellow #1', 'Fellow #2', 'Fellow #3']
    font = pg.font.Font('8201.ttf', 23)
    count = 0
    for i in range(4):
        screen.blit(font.render(data[i], False, border_color), (width // 2 - width // 10, 100 + count))
        count += 70
    pg.display.flip()

#   For text on each button

def output_text(screen):
    font = pg.font.Font('8201.ttf', 23)
    data_1, data_2, data_3 = 'Snake', 'About Us', 'Quit'
    screen.blit(font.render(data_1, False, color), (width // 2 - width // 10 + 20, 100))
    screen.blit(font.render(data_2, False, color), (width // 2 - width // 10 + 5, 170))
    screen.blit(font.render(data_3, False, color), (width // 2 - width // 10 + 28, 243))

#   Menu

def menu(screen):
    pg.display.set_caption('Menu')
    screen.fill(color)
    create_border(screen)

    #   Start button
    pg.draw.rect(screen, border_color, (width // 2 - width // 10, 90, 100, 50))

    #   About us
    pg.draw.rect(screen, border_color, (width // 2 - 50, 160, 100, 50))

    #   Quit button
    pg.draw.rect(screen, border_color, (width // 2 - 50, 230, 100, 50))

    output_text(screen)
    pg.display.flip()
    gameover = False
    while not gameover:
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                gameover = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pos()[0] >= width // 2 - width // 10 and pg.mouse.get_pos()[1] >= 230:
                    if pg.mouse.get_pos()[0] <= width // 2 + width // 10 and pg.mouse.get_pos()[1] <= 280:
                            sys.exit()
                elif pg.mouse.get_pos()[0] >= width // 2 - width // 10 and pg.mouse.get_pos()[1] >= 160:
                    if pg.mouse.get_pos()[0] <= width // 2 + width // 10 and pg.mouse.get_pos()[1] <= 210:
                        about_us(screen)
                elif pg.mouse.get_pos()[0] >= width // 2 - width // 10 and pg.mouse.get_pos()[1] >= 90:
                    if pg.mouse.get_pos()[0] <= width // 2 + width // 10 and pg.mouse.get_pos()[1] <= 140:
                            startGame(screen)

def main():
    pg.init()
    pg.font.init()
    screen = pg.display.set_mode(size)
    menu(screen)

if __name__ == '__main__':
    main()
