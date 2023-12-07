import pygame
import os

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Group Example")

# Define colors
white = (255, 255, 255)

# Define image names
image_names = [
    "beef", "broccoli", "cheese", "chicken", "cream", "egg", "fish", 
    "flour", "ham", "milk", "misopaste", "oil", "onion", "potato", 
    "rice", "spinach", "sugar", "sushivinegar", "tofu", "tomato"
]

# Load images
image_folder = (r"C:\Users\user\Desktop\python-games\UROP\images")  
images = {name: pygame.image.load(os.path.join(image_folder, f"{name}.png")) for name in image_names}

# Create sprite class
class FoodSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = col * (self.rect.width + 10)
        self.rect.y = row * (self.rect.height + 10)

    def update(self):
        if self.dragging:
            self.rect.center = pygame.mouse.get_pos()
        
# Create sprite group
food_group = pygame.sprite.Group()

for row in range(4):
    for col in range(5):
        index = row * 5 + col
        if index < len(image_names):
            food_sprite = FoodSprite(images[image_names[index]], row, col)
            food_group.add(food_sprite)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in food_group:
                if sprite.rect.collidepoint(event.pos):
                    sprite.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for sprite in food_group:
                sprite.dragging = False

    # Update sprites
    food_group.update()

    # Clear the screen
    screen.fill(white)

    # Draw sprites
    food_group.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()