import pygame
import numpy as np

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1200, 1200))
clock = pygame.time.Clock()
running = True

# Grid blocks size
block_width = 10
block_height = 10
block_margin = 2  # Margin between blocks of the grid


def grid_generation(num_blocks: int, height: int, width: int, margin: int) -> list:
    """
    Generates the grid for the game visualization
    """
    grid = list()
    for row in range(num_blocks):
        grid.append([])
        for column in range(num_blocks):
            grid[row].append(0)
 
    # Printing the grid
    for row in range(num_blocks):
        for column in range(num_blocks):
            color = "darkgrey"
            pygame.draw.rect(screen,
                             color,
                             [(margin + width) * column + margin,
                              (margin + height) * row + margin,
                              width,
                              height]
                             )
    return grid


# pygame loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing the grid
    screen.fill("black")

    grid_generation(num_blocks=100, block_height, block_width, block_margin)
 

    # Displaying the game
    grid = pygame.display.flip()

    clock.tick(60)  # Limited to 60 fps

pygame.quit()
