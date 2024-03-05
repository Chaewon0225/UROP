import os
import pygame
from pygame import mixer
import pgzrun

pygame.init()

#mixer.music.load('backgroundmusic.mp3')
#mixer.music.play(-1)

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

image_dict = {}

directory_path= r"/Users/user/Desktop/UROP/images"

food_list = [
    'cupcakes.png', 'frenchfries.png', 'milkshake.png', 'cheesestick.png', 'friedchicken.png',
    'onionrings.png', 'cheesepizza.png', 'friedrice.png', 'donut.png', 'cheesefries.png',
    'misosoup.png', 'omelet.png', 'tofubowl.png', 'steak.png', 'veggiestew.png', 'meatloaf.png',
    'cobbsalad.png', 'beefcurry.png', 'sushi.png', 'grilledfish.png', 
]

for food_image in food_list:
    full_path = os.path.join(directory_path, food_image)
    image_name = food_image.split('.')[0]
    image_dict[image_name] = pygame.image.load(full_path)
    # Get the rect for the image
    image_rect = image_dict[image_name].get_rect()
    # Set the center of the rect to be the center of the screen
    image_rect.center = (1000 // 2, 600 // 2)  # Adjust 800 and 600 according to your screen size
    image_dict[image_name + '_rect'] = image_rect

###################################################################################################
tip_list = ['1_spinach.png', '1_tofu.png', '2_beef.png', '2_onion.png', '3_fish.png', '3_rice.png', 
            '4_spinach.png', '4_tofu.png', '5_ham.png', '5_tomato.png', '6_egg.png', '6_tomato.png',
            '7_fish.png', '7_rice.png', '8_flour.png', '8_oil.png', '9_sugar.png', '10_cream.png',
            '10_sugar.png', '11_cheese.png', '11_tomato.png', '12_beef.png', '12_onion.png']

for tip_image in tip_list:
    full_path = os.path.join(directory_path, tip_image)
    image_name = food_image.split('.')[0]
    image_dict[image_name] = pygame.image.load(full_path)
    # Get the rect for the image
    image_rect = image_dict[image_name].get_rect()
    # Set the center of the rect to be the center of the screen
    image_rect.center = (300, 20)  # Adjust 800 and 600 according to your screen size
    image_dict[image_name + '_rect'] = image_rect

stage_list = ['stage1.png', 'stage2.png', 'stage3.png', 'stage4.png', 'stage5.png', 'stage6.png',
              'stage7.png', 'stage8.png', 'stage9.png', 'stage10.png', 'stage11.png', 'stage12.png']

for stage_image in stage_list:
    full_path = os.path.join(directory_path, stage_image)
    image_name = food_image.split('.')[0]
    image_dict[image_name] = pygame.image.load(full_path)
    # Get the rect for the image
    image_rect = image_dict[image_name].get_rect()
    # Set the center of the rect to be the center of the screen
    image_rect.center = (20, 20)  # Adjust 800 and 600 according to your screen size
    image_dict[image_name + '_rect'] = image_rect

foodCooked = False

image_names = r"/Users/user/Desktop/UROP/images"
images = {name: pygame.image.load(os.path.join(image_names, name)) for name in image_list}

cookingFail = False

emptyHeart_image = pygame.image.load("empty heart.png")
fullHeart_image = pygame.image.load("full heart.png")

emptyHeart_rect = emptyHeart_image.get_rect(topleft=(778, 130))
emptyHeart2_rect = emptyHeart_image.get_rect(topleft=(808, 130))
emptyHeart3_rect = emptyHeart_image.get_rect(topleft=(838, 130))
emptyHeart4_rect = emptyHeart_image.get_rect(topleft=(868, 130))
emptyHeart5_rect = emptyHeart_image.get_rect(topleft=(898, 130))

heartMeter = 0

fullHeart_rect = fullHeart_image.get_rect(topleft=(778, 130))
fullHeart2_rect = fullHeart_image.get_rect(topleft=(808, 130))
fullHeart3_rect = fullHeart_image.get_rect(topleft=(838, 130))
fullHeart4_rect = fullHeart_image.get_rect(topleft=(868, 130))
fullHeart5_rect = fullHeart_image.get_rect(topleft=(898, 130))


overlay_image = pygame.image.load("empty gauge.png")
overlay2_image = pygame.image.load("empty gauge.png")
overlay3_image = pygame.image.load("empty gauge.png")
# Resize overlay image
scale_factor = 0.06
overlay_image = pygame.transform.scale(overlay_image, (int(overlay_image.get_width() * scale_factor), int(overlay_image.get_height() * scale_factor)))
overlay2_image = pygame.transform.scale(overlay2_image, (int(overlay2_image.get_width() * scale_factor), int(overlay2_image.get_height() * scale_factor)))
overlay3_image = pygame.transform.scale(overlay3_image, (int(overlay3_image.get_width() * scale_factor), int(overlay3_image.get_height() * scale_factor)))


RECT_WIDTH, RECT_HEIGHT = 250, 150
rect_x = (WIDTH - RECT_WIDTH) // 2  # Centering the rectangle horizontally
rect_y = (HEIGHT - RECT_HEIGHT) // 2  # Centering the rectangle vertically

button_rect = Rect(rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)
button_visible = True  # Flag to track button visibility
draw_rectangles = False  # Flag to control drawing of rectangles

overlay_rect = overlay_image.get_rect(topleft=(778, 18))
overlay2_rect = overlay2_image.get_rect(topleft=(778, 53))
overlay3_rect = overlay3_image.get_rect(topleft=(778, 88))

fridge_rect = Rect(0, 125, 198, 475)  # fridge
fridgeOverlay_image = pygame.image.load("fridge interface.png")
fridgeOverlay_image = pygame.transform.scale(fridgeOverlay_image, (int(fridgeOverlay_image.get_width() * 0.80), int(fridgeOverlay_image.get_height() * 1)))
fridgeOverlay_rect = fridgeOverlay_image.get_rect(topleft=(0,0))
#fridgeOverlay_rect = Rect(200, 100, 600, 400)
fridgeOverlayActive = False
fridgeExit_image = pygame.image.load("Red X.png")
scale_factorFridge = 0.125
#fridgeExit_image = pygame.transform.scale(fridgeExit_image, (int(fridgeExit_image.get_width() * scale_factorFridge), int(fridgeExit_image.get_height() * scale_factorFridge)))
#fridgeExit_rect = fridgeExit_image.get_rect(topleft=(287 , 3))

##########################################################################################
tip_rect = Rect(10, 150, 50, 50)
tipOverlay_image = pygame.image.load("1_spinach.png")
tipOverlay_image = pygame.transform.scale(tipOverlay_image, (int(tipOverlay_image.get_width() * 0.5), int(fridgeOverlay_image.get_height() * 0.5)))
tipOverlay_rect = tipOverlay_image.get_rect(topleft=(100,100))
tipOverlayActive = False

cookbook_rect = Rect(700, 400, 100, 25)  # cookbook

stage_image = pygame.image.load("stage1.png")
scale_factorstage = 0.75
stage_image = pygame.transform.scale(stage_image, (int(stage_image.get_width() * scale_factorstage), int(stage_image.get_height() * scale_factorstage)))
stage_rect = stage_image.get_rect(center=(20, 20))

gauge1_rect = Rect(783, 20, 10, 25)
gauge2_rect = Rect(783, 55, 10, 25)
gauge3_rect = Rect(783, 90, 10, 25)

cook_image = pygame.image.load("cook button.png")
scale_factorcook = 0.75
cook_image = pygame.transform.scale(cook_image, (int(cook_image.get_width() * scale_factorcook), int(cook_image.get_height() * scale_factorcook)))
cook_rect = cook_image.get_rect(center=(475,415))

cookingFail_image = pygame.image.load("cooking failed.png")
cookingFail_image = pygame.transform.scale(cookingFail_image, (int(cookingFail_image.get_width() * 1.5), int(cookingFail_image.get_height() * 1.5)))
cookingFail_rect = cookingFail_image.get_rect(center=(500,300))

class FoodSprite(pygame.sprite.Sprite):
    def __init__(self, image, filename, x, y):
        super().__init__()
        self.image = image
        self.filename = filename  # Store the filename
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

food_group = pygame.sprite.Group()

# Define number of rows and columns
rows = 5
cols = 4

for row in range(rows):
    for col in range(cols):
        index = row * cols + col
        if index < len(image_names):
            filename = image_list[index]
            food_sprite = FoodSprite(images[filename], filename, col * (RECT_WIDTH - 180) + 23, row * (RECT_HEIGHT - 52) + 135)
            food_group.add(food_sprite)

class Fridge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

###########################################################
        
class Tip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((200, 200))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

class Stage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((200, 200))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

scaled_food_group = pygame.sprite.Group()

# Scale factor (adjust as needed)
scale_factorS = 1

for food_sprite in food_group:
    # Scale each sprite
   scaled_sprite = FoodSprite(pygame.transform.scale(food_sprite.image, (int(food_sprite.rect.width * scale_factorS), int(food_sprite.rect.height * scale_factorS))),
                               food_sprite.filename,  # Copy the filename from the original sprite
                               int(food_sprite.rect.x * scale_factorS),
                               int(food_sprite.rect.y * scale_factorS)),
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
o_key_pressed = False
o_key_val = 0
p_key_pressed = False
p_key_val = 0


def draw():
    screen.blit(background_images[current_background], (0, 0))
    if draw_rectangles and button_visible == False:  # If not visible and flag set, draw the rectangles
        screen.blit(overlay_image, overlay_rect)
        screen.blit(overlay2_image, overlay2_rect)
        screen.blit(overlay3_image, overlay3_rect)

        screen.blit(emptyHeart_image, emptyHeart_rect)
        screen.blit(emptyHeart_image, emptyHeart2_rect)
        screen.blit(emptyHeart_image, emptyHeart3_rect)
        screen.blit(emptyHeart_image, emptyHeart4_rect)
        screen.blit(emptyHeart_image, emptyHeart5_rect)

        screen.blit(stage_image, stage_rect)

        screen.draw.text("I feel hungry... Let's open the fridge.", center=(500, 50), color='white', fontsize=30)

        screen.draw.filled_rect(cookbook_rect, 'white')
        screen.draw.text("COOKBOOK", center=cookbook_rect.center, color='black', fontsize=20)
        screen.draw.filled_rect(gauge1_rect, 'orange')
        screen.draw.text("SATIATION", center=overlay_rect.center, color='black', fontsize=22)
        screen.draw.filled_rect(gauge2_rect, 'green')
        screen.draw.text("SATISFACTION", center=overlay2_rect.center, color='black', fontsize=22)
        screen.draw.filled_rect(gauge3_rect, 'yellow')
        screen.draw.text("NUTRITION", center=overlay3_rect.center, color='black', fontsize=22)

    if heartMeter == 1:
        screen.blit(fullHeart_image, fullHeart_rect)
    if heartMeter == 2:
        screen.blit(fullHeart_image, fullHeart_rect)
        screen.blit(fullHeart_image, fullHeart2_rect)
    if heartMeter == 3:
        screen.blit(fullHeart_image, fullHeart_rect)
        screen.blit(fullHeart_image, fullHeart2_rect)
        screen.blit(fullHeart_image, fullHeart3_rect)
    if heartMeter == 4:
        screen.blit(fullHeart_image, fullHeart_rect)
        screen.blit(fullHeart_image, fullHeart2_rect)
        screen.blit(fullHeart_image, fullHeart3_rect)
        screen.blit(fullHeart_image, fullHeart4_rect)
    if heartMeter == 5:
        screen.blit(fullHeart_image, fullHeart_rect)
        screen.blit(fullHeart_image, fullHeart2_rect)
        screen.blit(fullHeart_image, fullHeart3_rect)
        screen.blit(fullHeart_image, fullHeart4_rect)
        screen.blit(fullHeart_image, fullHeart5_rect)

    if fridgeOverlayActive and draw_rectangles and button_visible == False:
        screen.blit(fridgeOverlay_image, fridgeOverlay_rect)
        screen.blit(tipOverlay_image, tipOverlay_rect)
        scaled_food_group.draw(screen.surface)
        if current_target_index == 3:
            screen.blit(cook_image, cook_rect)
        if emptyHeart3_rect == 'fullHeart.png':
            screen.blit(tip_image, tip_rect)
            
    if foodCooked:
        if target_image_name in image_dict:
                image_surface = image_dict[target_image_name]
                rect_name = target_image_name + '_rect'
                screen.blit(image_surface, image_dict[rect_name].topleft)

    if cookingFail:
        screen.blit(cookingFail_image,cookingFail_rect)
        
             


removed_sprites_count = 0
sprites_in_hand = list(food_group)[:3]  # Assuming you want the first 3 sprites
hand_sprites_count = len(sprites_in_hand)
target_locations = [(380, 260), (450, 260), (515, 255)]

selected_sprite_filenames = []
images_rev = {v: k for k, v in images.items()}


for sprite, target_location in zip(sprites_in_hand, target_locations):
    sprite.rect.topleft = target_location


current_target_index = 0


def on_mouse_down(pos):
    global current_background, button_visible,draw_rectangles
    if button_rect.collidepoint(pos) and button_visible:
        current_background = (current_background + 1) % len(background_images)
        button_visible = False  # Hide the button once it's pressed
    global fridge_rect
    global fridgeOverlayActive
    if fridge_rect.collidepoint(pos) and draw_rectangles and button_visible == False: 
         fridgeOverlayActive = True

    global fridgeExit_rect
    #if fridgeExit_rect.collidepoint(pos):
         #fridgeOverlayActive = False

    clicked_sprites = [sprite for sprite in scaled_food_group if sprite.rect.collidepoint(pos)]
    for sprite in clicked_sprites:
        if fridgeOverlayActive and button_visible == False:
            global removed_sprites_count, current_target_index
            if current_target_index < len(target_locations):
                target_location = target_locations[current_target_index]
                sprite.rect.x, sprite.rect.y = target_location
                current_target_index += 1
                removed_sprites_count += 1
                filename = sprite.filename  # Access the stored filename
                selected_sprite_filenames.append(filename)
                print(selected_sprite_filenames)
    if cook_rect.collidepoint(pos):
        recipies()
       
def recipies():   
        global foodCooked, cookingFail, target_image_name, fridgeOverlayActive
        #Beef as first option
        if selected_sprite_filenames[0] == 'beef.png':
            if selected_sprite_filenames[1] == 'broccoli.png':
                if selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'steak'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'onion.png':
                if selected_sprite_filenames[2] == 'broccoli.png':
                    target_image_name = 'steak'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'meatloaf'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'rice.png':
                    target_image_name = 'beefcurry'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'flour.png':
                if selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'meatloaf'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'rice.png':
                if selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'beefcurry'
                    foodCooked = True 
        #Broccoli as first option
        elif selected_sprite_filenames[0] == 'broccoli.png':
            if selected_sprite_filenames[1] == 'beef.png':
                if selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'steak'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'onion.png':
                if selected_sprite_filenames[2] == 'beef.png':
                    target_image_name = 'steak'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'fish.png':
                    target_image_name = 'grilledfish'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'tomato.png':
                    target_image_name = 'veggiestew'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'fish.png':
                if selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'grilledfish'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'tomato.png':
                if selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'veggiestew'
                    foodCooked = True
        #Cheese as first option
        elif selected_sprite_filenames[0] == 'cheese.png':
            if selected_sprite_filenames[1] == 'flour.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'cheesestick'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'tomato.png':
                    target_image_name = 'cheesepizza'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'sugar.png':
                    target_image_name = 'cheesecake'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'oil.png':
                if selected_sprite_filenames[2] == 'potato.png':
                    target_image_name = 'cheesefries'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'cheesestick'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'potato.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'cheesefries'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'tomato.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'cheesepizza'
                    foodCooked = True            
        #Chicken as first option
        elif selected_sprite_filenames[0] == 'chicken.png':
            if selected_sprite_filenames[1] == 'flour.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'friedchicken'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'oil.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'friedchicken'
                    foodCooked = True                    
        #Cream as first option
        elif selected_sprite_filenames[0] == 'cream.png':
            if selected_sprite_filenames[1] == 'flour.png':
                if selected_sprite_filenames[2] == 'sugar.png':
                    target_image_name = 'cupcakes'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'sugar.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'cupcakes'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'milk.png':
                    target_image_name = 'milkshake'
                    foodCooked = True  
            elif selected_sprite_filenames[1] == 'milk.png':
                if selected_sprite_filenames[2] == 'sugar.png':
                    target_image_name = 'milkshake'
                    foodCooked = True                  
        #Egg as first option
        elif selected_sprite_filenames[0] == 'egg.png':
            if selected_sprite_filenames[1] == 'spinach.png':
                if selected_sprite_filenames[2] == 'tomato.png':
                    target_image_name = 'omelet'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'tomato.png':
                if selected_sprite_filenames[2] == 'spinach.png':
                    target_image_name = 'omelet'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'ham.png':
                    target_image_name = 'cobbsalad'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'milk.png':
                if selected_sprite_filenames[2] == 'sugar.png':
                    target_image_name = 'milkshake'
                    foodCooked = True  
            elif selected_sprite_filenames[1] == 'sugar.png':
                if selected_sprite_filenames[2] == 'milk.png':
                    target_image_name = 'milkshake'
                    foodCooked = True                
        #Fish as first option
        elif selected_sprite_filenames[0] == 'fish.png':
            if selected_sprite_filenames[1] == 'rice.png':
                if selected_sprite_filenames[2] == 'sushivinegar.png':
                    target_image_name = 'sushi'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'sushivinegar.png':
                if selected_sprite_filenames[2] == 'rice.png':
                    target_image_name = 'sushi'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'broccoli.png':
                if selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'grilledfish'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'onion.png':
                if selected_sprite_filenames[2] == 'broccoli.png':
                    target_image_name = 'grilledfish'
                    foodCooked = True                 
        #Flour as first option
        elif selected_sprite_filenames[0] == 'flour.png':
            if selected_sprite_filenames[1] == 'oil.png':
                if selected_sprite_filenames[2] == 'potato.png':
                    target_image_name = 'frenchfries'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'cheese.png':
                    target_image_name = 'cheesestick'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'chicken.png':
                    target_image_name = 'friedchicken'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'onionrings'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'sugar.png':
                    target_image_name = 'donuts'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'potato.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'frenchfries'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'chicken.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'friedchicken'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'onion.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'onionrings'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'beef':
                    target_image_name = 'meatloaf'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'sugar.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'donuts'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'cream.png' or 'milk.png':
                    target_image_name = 'cupcakes'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'beef.png':
                if selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'meatloaf'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'cheese.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'cheesestick'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'tomato.png':
                    target_image_name = 'cheesepizza'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'sugar.png':
                    target_image_name = 'cheesecake'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'sugar.png':
                if selected_sprite_filenames[2] == 'cream.png' or 'milk.png':
                    target_image_name = 'cupcakes'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'cheese.png':
                    target_image_name = 'cheesecake'
                    foodCooked = True                         
        #Ham as first option
        elif selected_sprite_filenames[0] == 'ham.png':
            if selected_sprite_filenames[1] == 'rice.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'friedrice'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'oil.png':
                if selected_sprite_filenames[2] == 'rice.png':
                    target_image_name = 'friedrice'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'tomato.png':
                if selected_sprite_filenames[2] == 'egg.png':
                    target_image_name = 'cobbsalad'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'egg.png':
                if selected_sprite_filenames[2] == 'tomato.png':
                    target_image_name = 'cobbsalad'
                    foodCooked = True
        #Milk as first option
        elif selected_sprite_filenames[0] == 'milk.png':
            if selected_sprite_filenames[1] == 'sugar.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'cupcakes'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'cream.png' or 'egg.png':
                    target_image_name = 'milkshake'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'cream.png' or 'egg.png':
                if selected_sprite_filenames[2] == 'sugar.png':
                    target_image_name = 'milkshake'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'cream.png' or 'milk.png':
                if selected_sprite_filenames[2] == 'sugar.png':
                    target_image_name = 'cupcakes'
                    foodCooked = True                
        #Misopaste as first option
        elif selected_sprite_filenames[0] == 'misopaste':
            if selected_sprite_filenames[1] == 'spinach':
                if selected_sprite_filenames[2] == 'tofu':
                    target_image_name = 'misosoup'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'tofu':
                if selected_sprite_filenames[2] == 'spinach':
                    target_image_name = 'misosoup'
                    foodCooked = True            
        #Oil as first option
        elif selected_sprite_filenames[0] == 'oil.png':
            if selected_sprite_filenames[1] == 'ham.png':
                if selected_sprite_filenames[2] == 'rice.png':
                    target_image_name = 'friedrice'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'flour.png':
                if selected_sprite_filenames[2] == 'potato.png':
                    target_image_name = 'frenchfries'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'cheese.png':
                    target_image_name = 'cheesestick'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'sugar.png':
                    target_image_name = 'donuts'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'onionrings'  
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'chicken.png':
                    target_image_name = 'friedchicken'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'potato.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'frenchfries'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'cheese.png':
                    target_image_name = 'cheesefries'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'cheese.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'cheesestick'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'potato.png':
                    target_image_name = 'cheesefries'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'rice.png':
                if selected_sprite_filenames[2] == 'ham.png':
                    target_image_name = 'friedrice'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'chicken.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'friedchicken'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'onion.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'onionrings'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'sugar.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'donuts'
                    foodCooked = True
        #Onion as first option
        elif selected_sprite_filenames[0] == 'onion.png':
            if selected_sprite_filenames[1] == 'beef.png':
                if selected_sprite_filenames[2] == 'broccoli.png':
                    target_image_name = 'steak'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'meatloaf'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'rice.png':
                    target_image_name = 'beefcurry'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'broccoli.png':
                if selected_sprite_filenames[2] == 'beef.png':
                    target_image_name = 'steak'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'fish.png':
                    target_image_name = 'grilledfish'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'flour.png':
                if selected_sprite_filenames[2] == 'beef.png':
                    target_image_name = 'meatloaf'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'onionrings'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'rice.png':
                if selected_sprite_filenames[2] == 'beef.png':
                    target_image_name = 'beefcurry'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'fish.png':
                if selected_sprite_filenames[2] == 'broccoli.png':
                    target_image_name = 'grilledfish'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'oil.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'onionrings'
                    foodCooked = True            
        #Potato as first option
        elif selected_sprite_filenames[0] == 'potato.png':
            if selected_sprite_filenames[1] == 'oil.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'frenchfries'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'cheese.png':
                    target_image_name = 'cheesefries'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'flour.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'frenchfries'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'cheese.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'cheesefries'
                    foodCooked = True            
        #Rice as first option 
        elif selected_sprite_filenames[0] == 'rice.png':
            if selected_sprite_filenames[1] == 'beef.png':
                if selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'beefcurry'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'onion.png':
                if selected_sprite_filenames[2] == 'beef.png':
                    target_image_name = 'beefcurry'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'spinach.png':
                if selected_sprite_filenames[2] == 'tofu.png':
                    target_image_name = 'pokebowl'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'tofu.png':
                if selected_sprite_filenames[2] == 'spinach.png':
                    target_image_name = 'pokebowl'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'fish.png':
                if selected_sprite_filenames[2] == 'sushivinegar.png':
                    target_image_name = 'sushi'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'sushivinegar.png':
                if selected_sprite_filenames[2] == 'fish.png':
                    target_image_name = 'sushi'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'ham.png':
                if selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'friedrice'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'oil.png':
                if selected_sprite_filenames[2] == 'ham.png':
                    target_image_name = 'friedrice'
                    foodCooked = True                       
        #Spinach as first option
        elif selected_sprite_filenames[0] == 'spinach.png':
            if selected_sprite_filenames[1] == 'tofu.png':
                if selected_sprite_filenames[2] == 'misopaste.png':
                    target_image_name = 'misosoup'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'rice.png':
                    target_image_name = 'pokebowl'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'egg.png':
                if selected_sprite_filenames[2] == 'tomato.png':
                    target_image_name = 'omelet'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'misopaste.png':
                if selected_sprite_filenames[2] == 'tofu.png':
                    target_image_name = 'misosoup'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'rice.png':
                if selected_sprite_filenames[2] == 'tofu.png':
                    target_image_name = 'pokebowl'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'tomato.png':
                if selected_sprite_filenames[2] == 'egg.png':
                    target_image_name = 'omelet'
                    foodCooked = True       
        #Sugar as first option
        elif selected_sprite_filenames[0] == 'sugar.png':
            if selected_sprite_filenames[1] == 'flour.png':
                if selected_sprite_filenames[2] == 'cream.png' or 'milk.png':
                    target_image_name = 'cupcakes'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'cheese.png':
                    target_image_name = 'cheesecake'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'oil.png':
                    target_image_name = 'donuts'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'cream.png' or 'milk.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'cupcakes'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'cream.png' or 'egg.png':
                if selected_sprite_filenames[2] == 'milk.png':
                    target_image_name = 'milkshake'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'cheese.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'cheesecake'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'oil.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'donuts'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'milk.png':
                if selected_sprite_filenames[2] == 'cream.png' or 'egg.png':
                    target_image_name = 'milkshake'
                    foodCooked = True            
        #Sushi Vinegar as first option
        elif selected_sprite_filenames[0] == 'sushivinegar.png':
            if selected_sprite_filenames[1] == 'fish.png':
                if selected_sprite_filenames[2] == 'rice.png':
                    target_image_name = 'sushi'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'rice.png':
                if selected_sprite_filenames[2] == 'fish.png':
                    target_image_name = 'sushi'
                    foodCooked = True            
        #Tofu as first option
        elif selected_sprite_filenames[0] == 'tofu.png':
            if selected_sprite_filenames[1] == 'spinach.png':
                if selected_sprite_filenames[2] == 'misopaste.png':
                    target_image_name = 'misosoup'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'rice.png':
                    target_image_name = 'pokebowl'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'misopaste.png':
                if selected_sprite_filenames[2] == 'spinach.png':
                    target_image_name = 'misosoup'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'rice.png':
                if selected_sprite_filenames == 'spinach.png':
                    target_image_name = 'pokebowl'
                    foodCooked = True           
        #Tomato as first option
        elif selected_sprite_filenames[0] == 'tomato.png':
            if selected_sprite_filenames[1] == 'egg.png':
                if selected_sprite_filenames[2] == 'spinach':
                    target_image_name = 'omelet'
                    foodCooked = True
                elif selected_sprite_filenames[2] == 'ham.png':
                    target_image_name = 'cobbsalad'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'spinach.png':
                if selected_sprite_filenames[2] == 'egg.png':
                    target_image_name = 'omelet'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'ham.png':
                if selected_sprite_filenames[2] == 'egg.png':
                    target_image_name = 'cobbsalad'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'cheese.png':
                if selected_sprite_filenames[2] == 'flour.png':
                    target_image_name = 'cheesepizza'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'flour.png':
                if selected_sprite_filenames[2] == 'cheese.png':
                    target_image_name = 'cheesepizza'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'broccoli.png':
                if selected_sprite_filenames[2] == 'onion.png':
                    target_image_name = 'veggiestew'
                    foodCooked = True
            elif selected_sprite_filenames[1] == 'onion.png':
                if selected_sprite_filenames[2] == 'broccoli.png':
                    target_image_name = 'veggiestew'
                    foodCooked = True       
        else: 
            cookingFail = True
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
    global o_key_pressed
    if key == pygame.K_o:
        o_key_pressed = True
    global p_key_pressed
    if key == pygame.K_p:
        p_key_pressed = True

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
    global o_key_pressed
    if key == pygame.K_o:
        o_key_pressed = False
    global p_key_pressed
    if key == pygame.K_p:
        p_key_pressed = False

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
    global o_key_pressed, p_key_pressed,heartMeter
    if o_key_pressed and heartMeter < 5:
         heartMeter += 1
         o_key_pressed = False
    if p_key_pressed and heartMeter > 0:
         heartMeter -=1
         p_key_pressed = False

pgzrun.go()
