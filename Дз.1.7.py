import numpy as np
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 120
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
color = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]
t=[]
x=[]
y=[]
r=[]
a=[]
c=[]
c1=0

t0=[]
x0=[]
y0=[]
a0=[]
c0=[]
A=[]
B=[]
m=[]
n=[]
k=[]
G=0.0
H=0.0
v=0
for i in range(0, 5, 1):
    t.append(0.0)
    x.append(randint(100, 1100))
    y.append(randint(100, 600))
    r.append(randint(10, 100))
    a.append(randint(-100, 100))
    while c1 == 0:
        c1 = randint(-1, 1)
    c.append(c1)
    c1=0

for i in range(0, 5, 1):
    t0.append(0.0)
    x0.append(randint(100, 1100))
    y0.append(randint(100, 600))
    a0.append(randint(-100, 100))
    A.append(randint(100, 170))
    B.append(randint(100, 170))
    m.append(0)
    n.append(0.5*randint(2, 3))
    k.append(0)
    while c1 == 0:
        c1 = randint(-1, 1)
    c0.append(c1)
    c1=0
u = 100.0
b = 0.0
f = 0
def triangle(A, B, m, n, k, t, a, c, x, y, color):

    polygon(screen, color, [(x+a*t, y+c*(u**2-a*2)**0.5*t), (x+a*t + A*np.cos(k+m), y+c*(u**2-a*2)**0.5*t + A*np.sin(k+m)), (x+a*t + B*np.cos(k+n), y+c*(u**2-a*2)**0.5*t - B*np.sin(k+n))], 0)

    if (x + a * t >= 1200  or x+a*t + A*np.cos(k+m) >= 1200 or x+a*t + B*np.cos(k+n) >= 1200):
        x = x + a * t - 5
        y = y + c * (u ** 2 - a * 2) ** 0.5 * t
        t=0
        c = 0
        while c == 0:
            c = randint(-1, 1)
        a = randint(-100, 0)
    elif (x + a * t <= 0  or x+a*t + A*np.cos(k+m) <= 0 or x+a*t + B*np.cos(k+n) <= 0):
        x = x + a * t + 5
        y = y + c * (u ** 2 - a * 2) ** 0.5 * t
        t=0
        c = 0
        while c == 0:
            c = randint(-1, 1)
        a = randint(0, 100)
    elif (y+c*(u**2-a*2)**0.5*t >= 700 or y+c*(u**2-a*2)**0.5*t + A*np.sin(k+m) >= 700 or y+c*(u**2-a*2)**0.5*t - B*np.sin(k+n) >= 700):
        x = x + a * t
        y = y + c * (u ** 2 - a * 2) ** 0.5 * t - 5
        t=0
        a = randint(-100, 100)
        c=-1
    elif (y+c*(u**2-a*2)**0.5*t <= 0 or y+c*(u**2-a*2)**0.5*t + A*np.sin(k+m) <= 0 or y+c*(u**2-a*2)**0.5*t - B*np.sin(k+n) <= 0):
        x = x + a * t
        y = y + c * (u ** 2 - a * 2) ** 0.5 * t + 5
        t=0
        a = randint(-100, 100)
        c=1
    return k, t, a, c, x, y

def ball(t, a, c, x, y, r, color):
    circle(screen, color, (x+a*t, y+c*(u**2-a*2)**0.5*t), r)
    if (x + a * t >= 1200 - r):
        x = x + a * t - 5
        y = y + c * (u ** 2 - a * 2) ** 0.5 * t
        t=0
        c = 0
        while c == 0:
            c = randint(-1, 1)
        a = randint(-100, 0)
    elif (x + a * t <= r):
        x = x + a * t + 5
        y = y + c * (u ** 2 - a * 2) ** 0.5 * t
        t=0
        c = 0
        while c == 0:
            c = randint(-1, 1)
        a = randint(0, 100)
    elif (y+c*(u**2-a*2)**0.5*t >= 700-r):
        x = x + a * t
        y = y + c * (u ** 2 - a * 2) ** 0.5 * t - 5
        t=0
        a = randint(-100, 100)
        c=-1
    elif (y+c*(u**2-a*2)**0.5*t <= r):
        x = x + a * t
        y = y + c * (u ** 2 - a * 2) ** 0.5 * t + 5
        t=0
        a = randint(-100, 100)
        c=1
    return t, a, c, x, y
def face():
    rect(screen, (255, 255, 255), (0, 0, 400, 400), 0)
    circle(screen, (255, 255, 0), (200, 200), 150, 0)
    circle(screen, (255, 36, 0), (140, 170), 30, 15)
    circle(screen, (0, 0, 0), (140, 170), 15, 15)
    circle(screen, (255, 36, 0), (260, 170), 25, 15)
    circle(screen, (0, 0, 0), (260, 170), 15, 15)
    rect(screen, (0, 0, 0), (130, 270, 150, 30), 0)
    polygon(screen, (0, 0, 0), [(70, 70), (65, 75), (165, 155), (170, 150)], 0)
    polygon(screen, (0, 0, 0), [(330, 70), (335, 75), (235, 155), (230, 150)], 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    while i < 5:
        t[i]=t[i]+0.2
        t[i], a[i], c[i], x[i], y[i] = ball(t[i], a[i], c[i], x[i], y[i], r[i], color[i])
        i=i+1
    i=0
    while i < 5:
        k[i], t0[i], a0[i], c0[i], x0[i], y0[i] = triangle(A[i], B[i], m[i], n[i], k[i], t0[i], a0[i], c0[i], x0[i], y0[i], color[i])
        t0[i] = t0[i] + 0.05
        k[i]=k[i]+0.01*randint(1, 5)
        i=i+1
    i=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or 2 or 3:
                while i < 5:
                    if ((event.pos[0] - x[i] - a[i] * t[i]) ** 2 + (event.pos[1] - y[i] - c[i] * (u ** 2 - a[i] * 2) ** 0.5 * t[i]) ** 2 < r[i] ** 2):
                        f = f + 1
                        print('Your score is:')
                        print(f)
                        v=1
                    G=((event.pos[0]-(x0[i]+a0[i]*t0[i]))*(-B[i]*np.sin(k[i]+n[i]))-B[i]*np.cos(k[i]+n[i])*(event.pos[1]-(y0[i]+c0[i]*(u**2-a0[i]*2)**0.5*t0[i])))/(A[i]*np.cos(k[i]+m[i])*(-B[i]*np.sin(k[i]+n[i]))-B[i]*np.cos(k[i]+n[i])*(A[i]*np.sin(k[i]+m[i])))
                    H=(A[i]*np.cos(k[i]+m[i])*(event.pos[1]-(y0[i]+c0[i]*(u**2-a0[i]*2)**0.5*t0[i]))-(event.pos[0]-(x0[i]+a0[i]*t0[i]))*(A[i]*np.sin(k[i]+m[i])))/(A[i]*np.cos(k[i]+m[i])*(-B[i]*np.sin(k[i]+n[i]))-B[i]*np.cos(k[i]+n[i])*(A[i]*np.sin(k[i]+m[i])))
                    if (H > 0 and G > 0 and H + G < 1):
                        f = f + 2
                        print('Your score is:')
                        print(f)
                        v = 1
                    i = i + 1
                if v==0:
                    f=f-1
                    face()
                v=0
                i=0
                circle(screen, RED, event.pos, 5)
            pygame.display.update()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
print('Congratulations! Your IQ is:')
print(f)
print('Enter your name:')
yourname = raw_input()
p=0
d=[]
numb=[]
name=[]
score=[]
e=0

with open('champions.txt') as file:
    for line in file:
        if p%4==0:
            d = line
            numb.append(d)
        elif p%4==1:
            d = line
            name.append(d)
        elif p%4==2:
            d = line
            score.append(d)
        p=p+1
i=0
e=p/4
while i < p/4:
    if f >= int(score[i]):
        e = i
        i = p / 4
    i = i + 1



numb.append(p/4)
name.append(0)
score.append(0)


i=p/4
while i > e:
    i=i-1
    name[i + 1] = name[i]
    score[i + 1] = score[i]
name[e] = yourname
yourname='\n'+yourname
f=str(f)
f='\n'+f+'\n'
score[e] = f
numb[p/4]=p/4+1
numb[p/4]=str(numb[p/4])
numb[p/4]=numb[p/4]+'\n'
out = open('champions.txt', 'w')
for i in range(0, p/4+1, 1):
    out.write(str(numb[i]))
    out.write(str(name[i]))
    out.write(str(score[i]))
    out.write('\n')
