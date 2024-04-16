import pgzrun
from random import randint
from random import choice


TITLE = 'shark'
WIDTH = 518
HEIGHT = 800

playing = None
music.set_volume(0.5)

tracks = ['handel_mp3','handel_ogg']

bg = Actor('background.png')
fish = Actor('fish')
cave = Actor('cave')
vol =Actor('vol_on')
start=Actor('start')
fish.pos = (5, 748)
cave.x, cave.y = (450, 150)



coordinates = [(80, 93), (288, 176), (90, 258), (428, 293),
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
    coin.x = randint(20,500)
    coin.y = randint(50,700)
    coins.append(coin)

x, y = 0, 0
game_over = False
win = False
start_game = False
walk = True

points = 0

def draw():
    bg.draw()
    if start_game == False :
        start.image = 'start'
        start.pos = (480,30)
        start.draw()
    else:
        start.image = 'stop'
        start.pos = (480,30)
        start.draw()
        
    if start_game == True:
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
        screen.draw.text(f'Очки {points}', center=(WIDTH//2, 20), color='red', fontsize=40)
        '''if not playing:
            msg = 'Вкл музыку'
        else:
            msg = 'Выкл музыку '
        screen.draw.text(msg, fontsize=40, center=(80, 20), color='red')
        '''
        if not playing:
            vol.image = 'vol_on'
            vol.pos = (30,30)
            vol.draw()
        else:
            vol.image = 'vol_off'
            vol.pos = (30,30)
            vol.draw()
        


def update(dt):
    global game_over, win, points, playing
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
    #if fish.collidelist(obstacles) != -1:
    for obstacle in obstacles:
        if fish.colliderect(obstacle):
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
                if not playing:
                    sounds.scream.stop()
                else:
                    sounds.scream.play()
            else:
                obstacle.x += randint(50,100)
                if not playing:
                    sounds.scream.stop()
                else:
                    sounds.scream.play()
    


def on_key_down(key):
    global x, y
    global win , game_over
    if key == keys.RETURN:
        win = False
        game_over = False
        fish.pos = (5, 748)
    if key == keys.DOWN:
        y = 0.5
        walking()
    if key == keys.UP:
        y = -0.5
        walking()
    if key == keys.LEFT:
        x = -0.5
        walking()
    if key == keys.RIGHT:
        x = 0.5
        walking()



def on_mouse_down(pos):
    global playing, start_game
    if  vol.collidepoint(pos):
        if not playing:
            t = tracks.pop(0)
            music.play(t)
            playing = t
            tracks.append(t)
        else:
            music.stop()
            
    if  start.collidepoint(pos):
        if start_game == False :
            start_game = True
        else:
            start_game=False 
       
            

def on_music_end():
    global playing
    playing = None
    
    
def walking():
    global walk
    if walk:
        fish.image = "fish"
        walk = False
    else:
        fish.image = "fish2"
        walk = True



pgzrun.go()
