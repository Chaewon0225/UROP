from pygame import mixer
import pygame
import pgzrun
import sys

pygame.init()

mixer.music.load('backgroundmusic.mp3')
mixer.music.play(-1)

# Set up the display
screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Switch Background Example")

# Load background images
background_images = ["kitchen.png", "bedroom.png", "diningtable.png", "livingroom.png"]
current_background = 0  # Index of the current background image

# Create a button rect
button_rect = pygame.Rect(100, 100, 25, 25)  # Change position and size as needed
cook = Rect(500, 400, 100, 25)
fridge = Rect(300, 200, 150, 50)
cookbook = Rect(700, 400, 100, 25)
functions = [cook, fridge, cookbook]
cookw = Rect(300, 300, 300, 300)
fridgew = Rect(300, 300, 300, 300)
cookbookw = Rect(300, 300, 300, 300)
windows = [cookw, fridgew, cookbookw]

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                # Check if the mouse click is within the button_rect
                if button_rect.collidepoint(event.pos):
                    # Change to the next background image
                    current_background = (current_background + 1) % len(background_images)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the current background image
def draw():
    screen.blit(current_background, (0, 0))

    # Draw the button (a rectangle in this case)
    pygame.draw.rect(screen, (255, 0, 0), button_rect)  # Red button

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
pgzrun.go()

# Whatever we write down below will not run.
# Original codes for background and buttons
def draw():
    screen.blit("bedroom", (0, 0))
    screen.draw.filled_rect(cook, "gold")
    screen.draw.textbox("COOK", cook, color=("black"))
    screen.draw.filled_rect(fridge, "gold")
    screen.draw.textbox("Open the Fridge", fridge, color=("black"))
    screen.draw.filled_rect(cookbook, "gold")
    screen.draw.textbox("RECIPES", cookbook, color=("black"))
    def on_mouse_down(pos):
        for cook in functions:
            if cook.collidepoint(pos):
                screen.draw.filled_rect(cookw, "papaya whip")

# background music
# switch background
