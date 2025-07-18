import pygame, sys
from grid import Grid

pygame.init()

grey = "darkgrey"
width = 1200
height = 1200
cell_size = 15
fps = 60

cont = True

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic GoL")

clock = pygame.time.Clock()

grid = Grid(width, height, cell_size)


# Game Loop 
while cont:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            row = pos[1]  // cell_size
            column = pos[0] // cell_size
            simulation.toggle_cell(row, column)


    # Drawing 
    window.fill(grey)
    grid.draw(window)

    pygame.display.update()
    clock.tick(fps)
