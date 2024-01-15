from pygame import mixer
import pygame
import pgzrun
import sys

pygame.init()

mixer.music.load('backgroundmusic.mp3')
mixer.music.play(-1)

WIDTH, HEIGHT = 1000, 600

background_images = [
    'nutriquest.png',
    'kitchen.png',
    'bedroom.png',
    'livingroom.png',
    'diningtable.png'
]
current_background = 0

image_names = [
    "beef", "broccoli", "cheese", "chicken", "cream", "egg", "fish", 
    "flour", "ham", "milk", "misopaste", "oil", "onion", "potato", 
    "rice", "spinach", "sugar", "sushivinegar", "tofu", "tomato"
]

image_folder = (r"C:\Users\user\Desktop\UROP\images")  
images = {name: pygame.image.load(os.path.join(image_folder, f"{name}.png")) for name in image_names)

RECT_WIDTH, RECT_HEIGHT = 250, 150
rect_x = (WIDTH - RECT_WIDTH) // 2  # Centering the rectangle horizontally
rect_y = (HEIGHT - RECT_HEIGHT) // 2  # Centering the rectangle vertically

button_rect = Rect(rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)
button_visible = True  # Flag to track button visibility
draw_rectangles = False  # Flag to control drawing of rectangles

cook_rect = Rect(425, 400, 100, 25)  # cook
fridge_rect = Rect(25, 200, 150, 50)  # fridge
cookbook_rect = Rect(700, 400, 100, 25)  # cookbook

class FoodSprite(pygame.sprite.Sprite):
            def __init__(self, image, x, y):
              super().__init__()
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = col * (self.rect.width + 10)
            self.rect.y = row * (self.rect.height + 10)
            food_group = pygame.sprite.Group()
            for row in range(4):
                  for col in range(5):
                     index = row * 5 + col
                  if index < len(image_names):
                      food_sprite = FoodSprite(images[image_names[index]], row, col)
                      food_group.add(food_sprite)

class Fridge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))  # Change the size as needed
        self.image.fill((0, 0, 255))  # Blue color
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

food_group = pygame.sprite.Group()
fridge_group = pygame.sprite.Group()

fridge = Fridge()
fridge_group.add(fridge)
                      
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
        

pgzrun.go()
