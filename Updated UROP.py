import pgzrun

WIDTH, HEIGHT = 1000, 600

background_images = [
    'bedroom.png',
    'kitchen.png',
    'diningtable.png'
]
current_background = 0

RECT_WIDTH, RECT_HEIGHT = 250, 150
rect_x = (WIDTH - RECT_WIDTH) // 2  # Centering the rectangle horizontally
rect_y = (HEIGHT - RECT_HEIGHT) // 2  # Centering the rectangle vertically

button_rect = Rect(rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)
button_visible = True  # Flag to track button visibility
draw_rectangles = False  # Flag to control drawing of rectangles

cook_rect = Rect(425, 400, 100, 25)  # cook
fridge_rect = Rect(25, 200, 150, 50)  # fridge
cookbook_rect = Rect(700, 400, 100, 25)  # cookbook
#functions = [cook, fridge, cookbook]
#cookw = Rect(300, 300, 300, 300)
#fridgew = Rect(300, 300, 300, 300)
#cookbookw = Rect(300, 300, 300, 300)
#windows = [cookw, fridgew, cookbookw]

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
        
def on_mouse_up():
    global draw_rectangles
    draw_rectangles = True  # Set flag to draw rectangles
        

pgzrun.go()
