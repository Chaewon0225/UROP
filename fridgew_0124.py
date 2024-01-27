from pygame import mixer
import pygame
import pgzrun
import sys
import os

pygame.init()

width, height = 800, 600  # Adjust the dimensions as needed
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Image List')

image_list = [
    pygame.image.load('beef.png'),
    pygame.image.load('broccoli.png'),
    pygame.image.load('cheese.png'),
    pygame.image.load('chicken.png'),
    pygame.image.load('cream.png'),
    pygame.image.load('egg.png'),
    pygame.image.load('fish.png'),
    pygame.image.load('flour.png'),
    pygame.image.load('ham.png'),
    pygame.image.load('milk.png'),
    pygame.image.load('misopaste.png'),
    pygame.image.load('oil.png'),
    pygame.image.load('onion.png'),
    pygame.image.load('potato.png'),
    pygame.image.load('rice.png'),
    pygame.image.load('spinach.png'),
    pygame.image.load('sugar.png'),
    pygame.image.load('sushivinegar.png'),
    pygame.image.load('tofu.png'),
    pygame.image.load('tomato.png'),
]

rows, columns = 4, 5
image_width = 75
image_height = 75
index = 0

class ImageMatrix:
    def __init__(self, rows, columns, image_width, image_height):
        self.rows = rows
        self.columns = columns
        self.image_width = image_width
        self.image_height = image_height
        self.image_list = image_list

    def display_matrix(self, screen):
        for row in range(self.rows):
            for col in range(self.columns):
                index = row * self.columns + col
                x_position = col * self.image_width
                y_position = row * self.image_height
                screen.blit(self.image_list[index], (x_position, y_position))

image_matrix = ImageMatrix(rows, columns, image_width, image_height)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the image matrix
    image_matrix.display_matrix(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()