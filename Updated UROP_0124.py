from pygame import mixer
import pygame
import pgzrun
import sys
import os

pygame.init()

mixer.music.load('backgroundmusic.mp3')
mixer.music.play(-1)

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Image List')

background_images = [
    'nutriquest.png',
    'kitchen.png',
    'bedroom.png',
    'livingroom.png',
    'diningtable.png'
]
current_background = 0

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

RECT_WIDTH, RECT_HEIGHT = 250, 150
rect_x = (WIDTH - RECT_WIDTH) // 2  # Centering the rectangle horizontally
rect_y = (HEIGHT - RECT_HEIGHT) // 2  # Centering the rectangle vertically

button_rect = Rect(rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)
button_visible = True  # Flag to track button visibility
draw_rectangles = False  # Flag to control drawing of rectangles

cook_rect = Rect(425, 400, 100, 25)  # cook
fridge_rect = Rect(25, 200, 150, 50)  # fridge
cookbook_rect = Rect(700, 400, 100, 25)  # cookbook

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
                      
def draw():
    screen.blit(background_images[current_background], (0, 0))
    if button_visible:  # Draw the button only if it's visible
        screen.draw.filled_rect(button_rect, 'white')
        screen.draw.text("START GAME", center=button_rect.center, color='black', fontsize=50)
    elif draw_rectangles:  # If not visible and flag set, draw the rectangles
        screen.draw.filled_rect(cook_rect, 'white')
        screen.draw.text("COOK", center=cook_rect.center, color='black', fontsize=20)
        screen.draw.filled_rect(fridge_rect, 'white')
        screen.draw.text("FRIDGE", center=fridge_rect.center, color='black', fontsize=40)
        screen.draw.filled_rect(cookbook_rect, 'white')
        screen.draw.text("COOKBOOK", center=cookbook_rect.center, color='black', fontsize=20)

def on_mouse_down(pos):
    global current_background, button_visible
    if button_rect.collidepoint(pos) and button_visible:
        current_background = (current_background + 1) % len(background_images)
        button_visible = False  # Hide the button once it's pressed
    # When 'fridge' button is clicked, the group of ingredients shows up 
    if fridge_rect.collidepoint(pos) and button_visible:
       new_sprite = FoodSprite(images, 0, 0) 
                      
def on_mouse_up():
    global draw_rectangles
    draw_rectangles = True  # Set flag to draw rectangles



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
        