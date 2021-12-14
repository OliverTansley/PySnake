# Snake by Oliver Tansley
# Started 20/6/2021

# Dependencies
import pygame
from pygame.locals import *
import random

############################################################################################################################################
# Food class
############################################################################################################################################


class Food:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # Displays food by updating grid data
    def show(self, grid) -> None:
        grid.grid[self.x][self.y] = 3

############################################################################################################################################
# Snake class
############################################################################################################################################


class Snake:

    # Snake Direction Constants
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __init__(self) -> None:
        self.body = []
        self.length = 0
        self.x = 3
        self.y = 3
        self.facing = Snake.WEST

    # Displays snake to screen
    def show(self, grid) -> None:
        # Remove previous snake from the screen
        grid.clean()
        # Constrain snake head to the bounds of the screen
        if self.x > 9:
            self.x = 0
        if self.x < 0:
            self.x = 9
        if self.y > 9:
            self.y = 0
        if self.y < 0:
            self.y = 9

        # Display the snake head as red
        grid.grid[self.x][self.y] = 1

        # Constrain body to the bounds of the screen
        for i in self.body:
            if i[0] < 0:
                i[0] = 9
            if i[0] > 9:
                i[0] = 0
            if i[1] < 0:
                i[1] = 9
            if i[1] > 9:
                i[1] = 0

            # For each body part display this as green by updating the grid values
            grid.grid[i[0]][i[1]] = 2

    def move(self) -> None:
        # Temp variables for the heads current position
        currentx = self.x
        currenty = self.y

        # Move the head of the snake in the direction its facing
        if self.facing == Snake.SOUTH:
            self.y += 1
        elif self.facing == Snake.NORTH:
            self.y -= 1
        elif self.facing == Snake.WEST:
            self.x -= 1
        elif self.facing == Snake.EAST:
            self.x += 1

        # Iterate through each body part moving it ahead one in the chain
        for i in range(0, self.length-1):
            self.body[i] = self.body[i+1]

        # Update the first body part to be in the heads old position
        if self.length > 0:
            self.body[self.length-1] = [currentx, currenty]

    def addBod(self):
        # If there are no body parts add a new body part to the opposite side that the snake is facing
        if self.length == 0:
            if self.facing == Snake.NORTH:
                self.body.append([self.x, self.y - 1])
            elif self.facing == Snake.EAST:
                self.body.append([self.x - 1, self.y])
            elif self.facing == Snake.SOUTH:
                self.body.append([self.x, self.y + 1])
            elif self.facing == Snake.WEST:
                self.body.append([self.x + 1, self.y])
        # If there is a body part
        else:
            # Retrieve the end of the snakes tail
            end = self.body[self.length - 1]
            # Add the new body part to the end of the snake
            self.body.append(end)
        self.length += 1    # Increment the length variable

    def eat(self, food) -> None:
        # If the snakes head is on the same tile as the food
        if self.x == food.x and self.y == food.y:
            # Move the food
            food.x = random.randint(0, 9)
            food.y = random.randint(0, 9)
            # Increase the length of the snake
            self.addBod()

    def test(self) -> bool:
        # For each body part
        for i in self.body:
            # If the head is on the same tile as the body part
            if i[0] == self.x and i[1] == self.y:
                # End the game
                pygame.time.delay(1000)
                return False
        # Else keep playing
        return True

############################################################################################################################################
# Grid class
############################################################################################################################################


class Grid:

    # Color constants
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Construct 2D array to represent the grid
    def __init__(self) -> None:
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def show(self, screen) -> None:
        # Iterate through every position on the grid
        for i in range(0, 10):
            for j in range(0, 10):
                # Colour the grid based on the value stored at that position
                if self.grid[i][j] == 0:
                    pygame.draw.rect(screen, Grid.white,
                                     (i*70 + 2, j*70 + 2, 70 - 2, 70 - 2))
                elif self.grid[i][j] == 1:
                    pygame.draw.rect(screen, Grid.red,
                                     (i*70 + 2, j*70 + 2, 70 - 2, 70 - 2))
                elif self.grid[i][j] == 2:
                    pygame.draw.rect(screen, Grid.green,
                                     (i*70 + 2, j*70 + 2, 70 - 2, 70 - 2))
                elif self.grid[i][j] == 3:
                    pygame.draw.rect(screen, Grid.blue,
                                     (i*70 + 2, j*70 + 2, 70 - 2, 70 - 2))
                else:
                    pygame.draw.rect(screen, Grid.black,
                                     (i*70 + 2, j*70 + 2, 70 - 2, 70 - 2))

    def clean(self) -> None:
        # Iterate through grid values setting all to white
        for i in range(0, 10):
            for j in range(0, 10):
                self.grid[i][j] = 0


############################################################################################################################################
# Main
############################################################################################################################################


pygame.init()
# Initialise Screen
(width, height) = (700, 700)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
screen.fill((0, 0, 0))

s = Snake()
g = Grid()
f = Food(9, 9)
global running
running = True

while running:
    # Game tick speed
    pygame.time.delay(400)
    for event in pygame.event.get():

        # Close window on 'X' press
        if event.type == QUIT:
            running = False

        # Turn snake based on WASD keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                s.facing = Snake.NORTH
            if event.key == pygame.K_a:
                s.facing = Snake.WEST
            if event.key == pygame.K_s:
                s.facing = Snake.SOUTH
            if event.key == pygame.K_d:
                s.facing = Snake.EAST
    s.move()
    # Update game objects
    g.show(screen)
    s.show(g)
    f.show(g)
    s.eat(f)
    running = s.test()
    pygame.display.update()
pygame.quit()
