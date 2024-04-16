import pgzrun
from random import randint
from random import choice


TITLE = 'shark'
WIDTH = 518
HEIGHT = 800

#music.set_volume(0.5)
#music.play('hhavok-main')
playing = None

music.set_volume(0.5)

tracks = [
    'handel_mp3',
    'handel_ogg',
]

# Загрузка изображений
bg = Actor('background.png')
img = choice(['fish', 'fish2'])
fish = Actor(img)
cave = Actor('cave')
fish.pos = (5, 748)
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
        
coins = []
for i in range(10):
    coin = Actor('coin')
    coin.x = randint(0,500)
    coin.y = randint(0,700)
    coins.append(coin)

x, y = 0, 0
game_over = False
win = False
points = 0

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
    for coin in coins:
        coin.draw()
    screen.draw.text(f'Очки {points}', center=(WIDTH//2, 30), color='red', fontsize=40)
    if not playing:
        msg = 'Вкл музыку'
    else:
        msg = 'Выкл музыку '
    screen.draw.text(msg, fontsize=40, pos=(0, 20), color='red')


def update(dt):
    global game_over, win, points
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
    for coin in coins:
        if fish.colliderect(coin):
            coin.pos = (1000, 1000)
            points += 1  
    for obstacle in obstacles:
        if randint(0 , 1000) <1:
            obstacle.x += randint(-1,1) 
            if obstacle.image == 'shark':
                obstacle.x -= randint(50,100)
            else:
                obstacle.x += randint(50,100)
    


def on_key_down(key):
    global x, y
    global win , game_over
    if key == keys.RETURN:
        win = False
        game_over = False
        fish.pos = (5, 748)
    if key == keys.DOWN:
        y = 1
    if key == keys.UP:
        y = -1
    if key == keys.LEFT:
        x = -1
    if key == keys.RIGHT:
        x = 1



def on_mouse_down():
    global playing
    if not playing:
        t = tracks.pop(0)
        music.play(t)
        playing = t
        tracks.append(t)
    else:
        music.stop(t)


def on_music_end():
    global playing
    playing = None



pgzrun.go()
