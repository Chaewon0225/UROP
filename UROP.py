import pgzrun

WIDTH = 1000
HEIGHT = 600
FINAL_LEVEL = 12
BACKGROUND_IMAGES = ["bedroom.png", "livingroom.png"]
cook = Rect(500, 400, 100, 25)
fridge = Rect(300, 200, 150, 50)
cookbook = Rect(700, 400, 100, 25)
functions = [cook, fridge, cookbook]
cookw = Rect(300, 300, 300, 300)
fridgew = Rect(300, 300, 300, 300)
cookbookw = Rect(300, 300, 300, 300)
windows = [cookw, fridgew, cookbookw]

def draw():
    screen.blit("bedroom", (0, 0))
    screen.draw.filled_rect(cook, "gold")
    screen.draw.textbox("COOK", cook, color="black"))
    screen.draw.filled_rect(fridge, "gold")
    screen.draw.textbox("Open the Fridge", fridge, color="black")
    screen.draw.filled_rect(cookbook, "gold")
    screen.draw.textbox("RECIPES", cookbook, color="black")
    def on_mouse_down(pos):
for cook in functions:
            if cook.collidepoint(pos):
                screen.draw.filled_rect(cookw, "papaya whip")


def draw():
    screen.blit("kitchen", (0, 0))
    
pgzrun.go()
