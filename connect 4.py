import numpy, random, math
from copy import copy
print('1 for ai 0 for 2 player')
aiornot=bool(int(input()))
directions=((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1))
BOARD=[]
def index(n, f):
    for i in range(len(n)):
        if n[i]==f:
            return i
    #print(n, f)
    #print(not found)
for i in numpy.zeros((7, 6)).tolist():
    linejowifjo=[str(int(x)) for x in i]
    BOARD.append(linejowifjo)
def insert(board, column, turn):
    boavrd=board[::]
    try:
        boavrd[column][boavrd[column].index('0')]=turn
        if boavrd[column].index('0')<7:
            return (boavrd, 1)
        else:
            return (boavrd, 0)
    except:
        return (boavrd, 0)
def draw(board):
    global screen
    for x in range(50, len(board)*50+50, 50):
        for y in range(50, len(board[0])*50+50, 50):
            if board[int(x/50-1)][int(y/50-1)]=='1':
                pygame.draw.circle(screen, (255, 0, 0), (x, 400-y), 20)
            elif board[int(x/50-1)][int(y/50-1)]=='2':
                pygame.draw.circle(screen, (0, 0, 255), (x, 400-y), 20)
            else:
                pygame.draw.circle(screen, (255, 255, 255), (x, 400-y), 20)
def drop_coins(current, positions, starting):
    after=[x for x in current]
    for i in positions:
        try:
            after[i][index(after[i], '0')]=str(starting)
        except:
            return False
        starting=3-starting
    return after
def tree(Board):
    bottom=[]
    for i, o in list(numpy.ndenumerate(numpy.zeros((7,7,7,7,7)))):
        after=drop_coins(numpy.array(Board), i, 2)
        if after==False:
            continue
        else:
            bottom.append(score(after))
    return bottom

def minimax(bottomlevel, branches):
    MAIN=[bottomlevel]
    depth=(int(math.log(len(bottomlevel), branches)))
    maxormin=depth%2
    for i in range(depth):
        level=[]
        maxormin=1-maxormin
        for i in range(int(len(MAIN[-1])/branches)):
            if maxormin==0:
                level.append(max(MAIN[-1][i*branches:(i+1)*branches]))
            else:
                level.append(min(MAIN[-1][i*branches:(i+1)*branches]))
        MAIN.append(level)
    return MAIN

def check_for_end(board):
    for x in range(7):
        for y in range(7):
            try:
                if board[x][y]=='1':
                    for direction in ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)):
                        try:
                            if board[x+direction[0]][y+direction[1]]=='1' and board[x+direction[0]*2][y+direction[1]*2]=='1' and board[x+direction[0]*3][y+direction[1]*3]=='1' and x+direction[0]*3>=0 and y+direction[1]*3>=0:
                                #print(x, y, direction)
                                return 1
                            else:
                                continue
                        except:
                            continue
                elif board[x][y]=='2':
                    for direction in ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)):
                        try:
                            if board[x+direction[0]][y+direction[1]]=='2' and board[x+direction[0]*2][y+direction[1]*2]=='2' and board[x+direction[0]*3][y+direction[1]*3]=='2' and x+direction[0]*3>=0 and y+direction[1]*3>=0:
                                #print(x, y, direction)
                                return 2
                            else:
                                continue
                        except:
                            continue
            except:
                continue
    return 0

def check_for_3_row(board):
     for x in range(7):
        for y in range(7):
            try:
                if board[x][y]=='1':
                    for direction in ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)):
                        try:
                            if board[x+direction[0]][y+direction[1]]=='1' and board[x+direction[0]*2][y+direction[1]*2]=='1' and board[x+direction[0]*3][y+direction[1]*3]=='0' and x+direction[0]*3>=0 and y+direction[1]*3>=0:
                                #print(x, y, direction)
                                return 1
                            else:
                                continue
                        except:
                            continue
                elif board[x][y]=='2':
                    for direction in ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)):
                        try:
                            if board[x+direction[0]][y+direction[1]]=='2' and board[x+direction[0]*2][y+direction[1]*2]=='2' and board[x+direction[0]*3][y+direction[1]*3]=='0' and x+direction[0]*3>=0 and y+direction[1]*3>=0:
                                #print(x, y, direction)
                                return 2
                            else:
                                continue
                        except:
                            continue
            except:
                continue
     return 0

def check_for_2_row(board):
     for x in range(7):
        for y in range(7):
            try:
                if board[x][y]=='1':
                    for direction in ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)):
                        try:
                            if board[x+direction[0]][y+direction[1]]=='1' and board[x+direction[0]*2][y+direction[1]*2]=='0' and (board[x+direction[0]*3][y+direction[1]*3]=='0' or board[x+direction[0]*-1][y+direction[1]*-1]=='0') and x+direction[0]*3>=0 and y+direction[1]*3>=0:
                                #print(x, y, direction)
                                return 1
                            else:
                                continue
                        except:
                            continue
                elif board[x][y]=='2':
                    for direction in ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)):
                        try:
                            if board[x+direction[0]][y+direction[1]]=='2' and board[x+direction[0]*2][y+direction[1]*2]=='0' and (board[x+direction[0]*3][y+direction[1]*3]=='0' or board[x+direction[0]*-1][y+direction[1]*-1]=='0') and x+direction[0]*3>=0 and y+direction[1]*3>=0:
                                #print(x, y, direction)
                                return 2
                            else:
                                continue
                        except:
                            continue
            except:
                continue
     return 0



def score(BOARd):
    points=0
    if check_for_end(BOARd)==1:
        points+=-1000000000
    elif check_for_end(BOARd)==2:
        points+=10000000000000
    if check_for_3_row(BOARd)==2:
        points+=50
    elif check_for_3_row(BOARd)==1:
        points+=-30
    if check_for_2_row(BOARd)==2:
        points+=20
    elif check_for_2_row(BOARd)==1:
        points+=-10
    for i in range(7):
        for x in range(6):
            if BOARd[i][x]=='2':
                points+=-abs(3-i)/2
    return points
import pygame
from math import *
from pygame.locals import *
white=(255, 255, 255)
black=(0, 0, 0)
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 70)
pygame.init()
display_width = 400
display_height = 500
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('CONN4')
clock = pygame.time.Clock()
GameRun=True
redwin=False
bluewin=False
turn=0
while GameRun:
    screen.fill(black)
    click=pygame.mouse.get_pressed()
    mousePos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRun = False
        if event.type==MOUSEBUTTONDOWN:
            #print('yes')
            x=insert(BOARD, round(mousePos[0]/50)-1, str(turn+1))
            draw(BOARD)
            print(numpy.array(BOARD))
            screen.blit(myfont.render('Computing...', False, (255, 0, 0)), (0, 0))
            pygame.display.update()
            #print(round(mousePos[0]/50)-1)
            if x[1]:
                BOARD=x[0]
                if not aiornot:
                    turn=1-turn
                #ai is here
                if aiornot:
                    q=(minimax(tree(BOARD), 7))
                    print(q[-2])
                    x=insert(BOARD, q[-2].index(q[-1][0]), '2')
                    if x[1]:
                        BOARD=x[0]
                if (check_for_end(BOARD))==1:
                    redwinfont = myfont.render('Red Wins', False, (255, 0, 0))
                    redwin=True
                elif (check_for_end(BOARD))==2:
                    bluewinfont = myfont.render('Blue Wins', False, (0, 0, 255))
                    bluewin=True
            else:
                turn=1-turn
                                     
    draw(BOARD)
    if redwin:
        #screen.fill(black)
        screen.blit(redwinfont, (50, 200))
    elif bluewin:
        #screen.fill(black)
        screen.blit(bluewinfont, (50, 200))
    pygame.display.update()
    clock.tick(30)

pygame.quit()
