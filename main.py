import pgzrun
 
TITLE = "Platformer"
WIDTH = 800
HEIGHT = 400

bg = Actor("fon")
Hero = Actor("jump" ,(15,235))

def draw():
    bg.draw()
    Hero.draw()

def update():
    if keyboard.left:
        Hero.x = Hero.x - 5
    if keyboard.right:
        Hero.x = Hero.x + 5
        
def on_mouse_down(button, pos):
    pass


def on_mouse_up(button, pos):
    pass


def on_mouse_move(pos):
    pass


def on_key_down(key):
    pass


def on_key_up(key):
    pass
pgzrun.go()