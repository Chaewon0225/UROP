import os
import pygame
from pygame import mixer
import pgzrun

pygame.init()

mixer.music.load('backgroundmusic.mp3')
mixer.music.play(-1)

WIDTH, HEIGHT = 1000, 600

background_images = [
    'nutriquest.png',
    'kitchen.png',
    'bedroom.png',
    'diningtable.png'
]
current_background = 0

image_list = [
    'beef.png', 'broccoli.png', 'cheese.png', 'chicken.png', 'cream.png', 'egg.png',
    'fish.png', 'flour.png', 'ham.png', 'milk.png', 'misopaste.png', 'oil.png',
    'onion.png', 'potato.png', 'rice.png', 'spinach.png', 'sugar.png', 'sushivinegar.png',
    'tofu.png', 'tomato.png',
]

image_names = r"/Users/user/Desktop/UROP/images"
images = {name: pygame.image.load(os.path.join(image_names, name)) for name in image_list}

images = {name: pygame.image.load(os.path.join(image_names, name)) for name in image_list}


overlay_image = pygame.image.load("empty gauge.png")
overlay2_image = pygame.image.load("empty gauge.png")
overlay3_image = pygame.image.load("empty gauge.png")
overlay4_image = pygame.image.load("Stage 1.png")
# Resize overlay image
scale_factor = 0.06
overlay_image = pygame.transform.scale(overlay_image, (int(overlay_image.get_width() * scale_factor), int(overlay_image.get_height() * scale_factor)))
overlay2_image = pygame.transform.scale(overlay2_image, (int(overlay2_image.get_width() * scale_factor), int(overlay2_image.get_height() * scale_factor)))
overlay3_image = pygame.transform.scale(overlay3_image, (int(overlay3_image.get_width() * scale_factor), int(overlay3_image.get_height() * scale_factor)))
overlay4_image = pygame.transform.scale(overlay4_image, (int(overlay4_image.get_width() * scale_factor), int(overlay4_image.get_height() * scale_factor)))


RECT_WIDTH, RECT_HEIGHT = 250, 150
rect_x = (WIDTH - RECT_WIDTH) // 2  # Centering the rectangle horizontally
rect_y = (HEIGHT - RECT_HEIGHT) // 2  # Centering the rectangle vertically

button_rect = Rect(rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)
button_visible = True  # Flag to track button visibility
draw_rectangles = False  # Flag to control drawing of rectangles

overlay_rect = overlay_image.get_rect(topleft=(778, 18))
overlay2_rect = overlay2_image.get_rect(topleft=(778, 53))
overlay3_rect = overlay3_image.get_rect(topleft=(778, 88))
overlay4_rect = overlay4_image.get_rect(topleft=(200, 88))

cook_rect = Rect(425, 400, 100, 25)  # cook

fridge_rect = Rect(0, 125, 198, 475)  # fridge
fridgeOverlay_rect = Rect(200, 100, 600, 400)
fridgeOverlayActive = False
fridgeExit_image = pygame.image.load("Red X.png")
scale_factorFridge = 0.125
fridgeExit_image = pygame.transform.scale(fridgeExit_image, (int(fridgeExit_image.get_width() * scale_factorFridge), int(fridgeExit_image.get_height() * scale_factorFridge)))
fridgeExit_rect = fridgeExit_image.get_rect(topleft=(765 , 105))


cookbook_rect = Rect(700, 400, 100, 25)  # cookbook

gauge1_rect = Rect(783, 20, 10, 25)
gauge2_rect = Rect(783, 55, 10, 25)
gauge3_rect = Rect(783, 90, 10, 25)
stage_rect = Rect(15, 20, 15, 25)



class FoodSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

food_group = pygame.sprite.Group()

for row in range(4):
    for col in range(5):
        index = row * 5 + col
        if index < len(image_names):
            food_sprite = FoodSprite(images[image_list[index]], col * (RECT_WIDTH - 120) + 238, row * (RECT_HEIGHT - 60) + 150)
            food_group.add(food_sprite)

class Fridge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50



scaled_food_group = pygame.sprite.Group()

# Scale factor (adjust as needed)
scale_factorS = 0.95

for food_sprite in food_group:
    # Scale each sprite
    scaled_sprite = pygame.sprite.Sprite()
    scaled_sprite.image = pygame.transform.scale(food_sprite.image, (int(food_sprite.rect.width * scale_factorS), int(food_sprite.rect.height * scale_factorS)))
    scaled_sprite.rect = scaled_sprite.image.get_rect(topleft=(int(food_sprite.rect.x * scale_factorS), int(food_sprite.rect.y * scale_factorS)))
    scaled_food_group.add(scaled_sprite)


fridge_group = pygame.sprite.Group()
fridge = Fridge()
fridge_group.add(fridge)




# Flag to track whether 'A' key is pressed
a_key_pressed = False
a_key_val = 0
s_key_pressed = False
s_key_val = 0
d_key_pressed = False
d_key_val = 0
z_key_pressed = False
z_key_val = 0
x_key_pressed = False
x_key_val = 0
c_key_pressed = False
c_key_val = 0

def draw():
    screen.blit(background_images[current_background], (0, 0))
    if draw_rectangles and button_visible == False:  # If not visible and flag set, draw the rectangles
        screen.blit(overlay_image, overlay_rect)
        screen.blit(overlay2_image, overlay2_rect)
        screen.blit(overlay3_image, overlay3_rect)
        screen.blit(overlay4_image, overlay4_rect)
        screen.draw.filled_rect(cook_rect, 'white')
        screen.draw.text("COOK", center=cook_rect.center, color='black', fontsize=20)
        screen.draw.filled_rect(cookbook_rect, 'white')
        screen.draw.text("COOKBOOK", center=cookbook_rect.center, color='black', fontsize=20)
        screen.draw.filled_rect(gauge1_rect, 'orange')
        screen.draw.text("SATIATION", center=overlay_rect.center, color='black', fontsize=22)
        screen.draw.filled_rect(gauge2_rect, 'green')
        screen.draw.text("SATISFACTION", center=overlay2_rect.center, color='black', fontsize=22)
        screen.draw.filled_rect(gauge3_rect, 'yellow')
        screen.draw.text("NUTRITION", center=overlay3_rect.center, color='black', fontsize=22)
        screen.draw.filled_rect(stage_rect, 'orange')
    if fridgeOverlayActive:
         screen.draw.filled_rect(fridgeOverlay_rect, 'white')
         screen.blit(fridgeExit_image, fridgeExit_rect)
         scaled_food_group.draw(screen.surface)

def on_mouse_down(pos):
    global current_background, button_visible
    if button_rect.collidepoint(pos) and button_visible:
        current_background = (current_background + 1) % len(background_images)
        button_visible = False  # Hide the button once it's pressed
    global fridge_rect
    global fridgeOverlayActive
    if fridge_rect.collidepoint(pos):
         fridgeOverlayActive = True
    global fridgeExit_rect
    if fridgeExit_rect.collidepoint(pos):
         fridgeOverlayActive = False

def on_mouse_up():
    global draw_rectangles
    draw_rectangles = True  # Set flag to draw rectangles

def on_key_down(key):
    global a_key_pressed
    if key == pygame.K_a:
        a_key_pressed = True
    global s_key_pressed
    if key == pygame.K_s:
        s_key_pressed = True
    global d_key_pressed
    if key == pygame.K_d:
        d_key_pressed = True
    global z_key_pressed
    if key == pygame.K_z:
        z_key_pressed = True
    global x_key_pressed
    if key == pygame.K_x:
        x_key_pressed = True
    global c_key_pressed
    if key == pygame.K_c:
        c_key_pressed = True

def on_key_up(key):
    global a_key_pressed
    if key == pygame.K_a:
        a_key_pressed = False
    global s_key_pressed
    if key == pygame.K_s:
        s_key_pressed = False
    global d_key_pressed
    if key == pygame.K_d:
        d_key_pressed = False
    global z_key_pressed
    if key == pygame.K_z:
        z_key_pressed = False
    global x_key_pressed
    if key == pygame.K_x:
        x_key_pressed = False
    global c_key_pressed
    if key == pygame.K_c:
        c_key_pressed = False

def update():
    global a_key_pressed
    global a_key_val
    global z_key_val
    if a_key_pressed and a_key_val < 130:
            # Extend the length of gauge1_rect when 'A' key is pressed
            gauge1_rect.width += 13
            a_key_val += 13
            z_key_val -= 13
            a_key_pressed = False
    global s_key_pressed
    global s_key_val
    global x_key_val
    if s_key_pressed and s_key_val < 130:
            # Extend the length of gauge1_rect when 'A' key is pressed
            gauge2_rect.width += 13
            s_key_val += 13
            x_key_val -= 13
            s_key_pressed = False
    global d_key_pressed
    global d_key_val
    global c_key_val
    if d_key_pressed and d_key_val < 130:
            # Extend the length of gauge1_rect when 'A' key is pressed
            gauge3_rect.width += 13
            d_key_val += 13
            c_key_val -= 13
            d_key_pressed = False
    global z_key_pressed
    if z_key_pressed and z_key_val < 130 and a_key_val > 0:
            # Extend the length of gauge1_rect when 'A' key is pressed
            gauge1_rect.width -= 13
            a_key_val -= 13
            z_key_val += 13
            z_key_pressed = False
    global x_key_pressed
    if x_key_pressed and x_key_val < 130 and s_key_val > 0:
            # Extend the length of gauge1_rect when 'A' key is pressed
            gauge2_rect.width -= 13
            s_key_val -= 13
            x_key_val += 13
            x_key_pressed = False
    global c_key_pressed
    if c_key_pressed and c_key_val < 130 and d_key_val > 0:
            # Extend the length of gauge1_rect when 'A' key is pressed
            gauge3_rect.width -= 13
            d_key_val -= 13
            c_key_val += 13
            c_key_pressed = False

pgzrun.go()
