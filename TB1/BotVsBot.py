import pygame, random
from tkinter import messagebox, Tk
import bot.bot as bot
import bot.bot2 as bot2
import time

ORANGE = (255, 128, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (14, 45, 99)
PLIM = (241, 148, 138)
WIDTH = 15
HEIGHT = 15
MARGEN = 5
x = 0
cols = 50
rows = 50
grid = [[0 for i in range(cols)] for j in range(rows)]

for i in range(cols):
    for j in range(rows):
        if (i == j):
            lucky = random.randint(1, 4)
            if (lucky == 2):
                grid[j][i] = 1
        else:
            lucky = random.randint(1, 2)
            if (lucky == 2):
                grid[j][i] = 1


pygame.init()
window = [1000, 1000]
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Quoridor")
clock = pygame.time.Clock()

def main():
    start = (0, 0)
    finalBot = (0, 0)
    final = (49, 49)
    startBot = (49, 49)
    turn = 0
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 3:
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // (WIDTH + MARGEN)
                    row = pos[1] // (HEIGHT + MARGEN)
                    grid[row][col] = 1
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    turn = 1

        n = len(grid)
        for row in range(n):
            for col in range(n):
                color = WHITE
                if grid[row][col] == 1:
                    color = BLUE
                if grid[row][col] == 2:
                    color = GREEN
                if grid[row][col] == 3:
                    color = RED
                if grid[row][col] == 4:
                    color = ORANGE

                if grid[row][col] == 7:
                    color = PLIM
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGEN + WIDTH) * col + MARGEN,
                                  (MARGEN + HEIGHT) * row + MARGEN,
                                  WIDTH,
                                  HEIGHT])


        Route = bot.algorithm(grid, start, final, 2)
        path = Route.a_star()
        data1 = path[0]
        data2 = path[1]

        Route2 = bot2.algorithm(grid, startBot, finalBot, 3)
        path2 = Route2.a_star()
        data3 = path2[0]
        data4 = path2[1]


        if turn == 1:
            time.sleep(0.2)
            Movement = bot.movementBot(grid, data1, data2, x, 2)
            Movement.movement()
            start = Movement.movement()
            turn = 2


        if turn == 2:
            time.sleep(0.2)
            Movement2 = bot2.movementBot(grid, data3, data4, x, 3)
            Movement2.movement()
            startBot = Movement2.movement()
            turn = 1


        if (start == final):
            Tk().wm_withdraw()
            messagebox.showinfo("Resultado", "Bot verde gana")
        if (startBot == finalBot):
            Tk().wm_withdraw()
            messagebox.showinfo("Resultado", "Bot rojo gana")

        clock.tick(60)
        pygame.display.flip()
