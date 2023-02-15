import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []

next_dot = 0
timer = 0

for dot in range(0, 10) :
    actor = Actor('dot')
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

def draw() :
    screen.fill('black')
    number = 1

    for dot in dots :
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number = number + 1         # number += 1
    
    for line in lines :
        screen.draw.line(line[0], line[1], (102, 255, 153))

    screen.draw.text(str(round(timer, 2)), topleft=(10, 10), color=(0, 0, 102), fontsize=30)

def on_mouse_down(pos) :
    global next_dot
    global lines
    global dots

    if next_dot < 10 :          # 마지막 점을 누르고 또 눌러도 종료되지 않게 클릭수를 제한해둔다
        if dots[next_dot].collidepoint(pos) :
            if next_dot :
                lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
            next_dot = next_dot + 1
        else :
            lines = []          # 선의 위치를 초기화 시킨다
            next_dot = 0
            
            # 순서를 잘못 누르면 리셋되고 점들의 위치가 전부 바뀐다
            dots = []           # 점들의 위치를 초기화 시킨다
            for dot in range(0, 10) :       # 점들의 위치를 바꾼다
                actor = Actor('dot')
                actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
                dots.append(actor)


def update() :
    global timer
    global next_dot

    if(next_dot != 10) :
        timer += 1 / 60        

pgzrun.go()