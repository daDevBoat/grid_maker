"""
User instructions:

Change the num_of_rows and num_of_cols variables to the desired number, and then run the program.

The default grid layout consists of all zeroes (0). 
Press 0-9 to select what number should be placed in the grid. 
0 is blank, which basically makes it an eraser.

Press enter or close the window when done drawing. 
The grid will then be printed to the terminal.
"""
import pygame as pg
from pygame.locals import (K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_RETURN)
import math as m


pg.init()


num_of_cols = 10
num_of_rows = 10
block_size = None
screen_adjust = 50

if (pg.display.Info().current_h - screen_adjust) / num_of_rows < (pg.display.Info().current_w - screen_adjust) / num_of_cols:
    block_size = m.floor((pg.display.Info().current_h - screen_adjust) / num_of_rows)
else:
    block_size = m.floor((pg.display.Info().current_w - screen_adjust) / num_of_cols)

window_width = block_size * num_of_cols
window_height = block_size * num_of_rows

window = pg.display.set_mode([window_width, window_height])  # Lager spillvinduet
done = False
window.fill((255, 255, 255))


clock = pg.time.Clock()

default_input_num = 1

class Grid:
    def __init__(self, window, grid, input_num) -> None:
        self.window = window
        self.grid = grid
        self.input_num = input_num
        self.done = False
            
        
    def draw(self):
        for y in range(num_of_rows):
            for x in range(num_of_cols):
                if self.grid[y][x] != 0:
                    pg.draw.rect(self.window, (255 * self.grid[y][x] / 10, 255 * self.grid[y][x] / 10, 255 * self.grid[y][x] / 10), (x * block_size, y * block_size, block_size, block_size))
        
    def update(self):
        mouse_pressed = pg.mouse.get_pressed()
        key_pressed = pg.key.get_pressed()

        if mouse_pressed[0] or mouse_pressed[2]:
            mouse_pos = pg.mouse.get_pos()
            x = m.floor(mouse_pos[0] / block_size)
            y = m.floor(mouse_pos[1] / block_size)
            self.grid[y][x] = self.input_num


        if key_pressed[K_RETURN]:
            self.done = True

        if key_pressed[K_0]:
            self.input_num = 0
        elif key_pressed[K_1]:
            self.input_num = 1  
        elif key_pressed[K_2]:
            self.input_num = 2
        elif key_pressed[K_3]:
            self.input_num = 3  
        elif key_pressed[K_4]:
            self.input_num = 4
        elif key_pressed[K_5]:
            self.input_num = 5  
        elif key_pressed[K_6]:
            self.input_num = 6  
        elif key_pressed[K_7]:
            self.input_num = 7  
        elif key_pressed[K_8]:
            self.input_num = 8  
        elif key_pressed[K_9]:
            self.input_num = 9 
                   

grid = []

for y in range(num_of_rows):
    grid.append([])
    for x in range(num_of_cols):
        grid[-1].append(0)
        

created_grid = Grid(window, grid, default_input_num)

while not done:     # Selve kjøreløkken til spillet
    for event in pg.event.get():    # Hvis bruker trykker på X-symbolet øverst til høyre vil vinduet lukke og programmet slutte
        if event.type == pg.QUIT:
            created_grid.done = True

    created_grid.update()
    created_grid.draw()
    pg.display.flip()
    clock.tick(60)  # Setter FPS til 60
    window.fill((255, 255, 255))
    
    done = created_grid.done
pg.quit()


# Printing of the grid
print("[")
grid = created_grid.grid
for y in range(num_of_rows):
    print("[", end="")
    for x in range(num_of_cols):
        if x < num_of_cols - 1:
            print(f"{grid[y][x]},", end=" ")
        else:
            print(f"{grid[y][x]}", end="")
    if y < num_of_rows - 1:
        print("],")
    else:
        print("]")
print("]")
