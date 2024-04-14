import pgzrun
from random import choice


TITLE = 'In search of Nemo'
WIDTH = 518
HEIGHT = 800


# Загрузка изображений
bg = Actor('background.png')
fish = Actor('fish')
cave = Actor('cave')
fish.pos = (451, 748)
cave.x, cave.y = (450, 80)



coordinates = [(80, 63), (288, 176), (90, 258), (428, 293),
               (219, 388), (80, 528), (358, 541), (195, 691)]
obstacles = []
for coordinate in coordinates:
    if coordinate[0] > WIDTH//2 :
        obj = Actor('shark')
        obj.x = coordinate[0]
        obj.y = coordinate[1]
        obstacles.append(obj)
    else:
        obj = Actor('shark2')
        obj.x = coordinate[0]
        obj.y = coordinate[1]
        obstacles.append(obj)


x, y = 0, 0
game_over = False
win = False

def draw():
    bg.draw()
    if game_over:
        screen.draw.text(f'GAME OVER', center=(WIDTH//2, HEIGHT//2), color='red', fontsize=100)
        return
    if win:
        screen.draw.text(f'ПОБЕДА!', center=(WIDTH//2, HEIGHT//2), color='green', fontsize=100)
        return
    fish.draw()
    cave.draw()
    for obstacle in obstacles:
        obstacle.draw()


def update(dt):
    global game_over, win
    fish.x += x
    fish.y += y
    if fish.left < 0:
        fish.left = 0
    if fish.right > WIDTH:
        fish.right = WIDTH
    if fish.top < 0:
        fish.top = 0
    if fish.bottom > HEIGHT:
        fish.bottom = HEIGHT
    if fish.collidelist(obstacles) != -1:
        game_over = True
    if fish.colliderect(cave):
        win = True

def on_key_down(key):
    global x, y
    if key == keys.DOWN:
        y = 0.5
    if key == keys.UP:
        y = -0.5
    if key == keys.LEFT:
        x = -0.5
    if key == keys.RIGHT:
        x = 0.5


pgzrun.go()
