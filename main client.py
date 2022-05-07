import pygame, time, random, ctypes, socket, ast, numpy
from PIL import Image as image
from math import *
from PIL import Image

def convertImage(file):
    img = Image.open(file)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        elif item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(file, "PNG")
def convertImage2(file):
    img = Image.open(file)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item==datas[0]:
            newData.append((255, 255, 255, 0))
        
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(file, "PNG")
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
white=(255, 255, 255)
black=(0, 0, 0)
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
scorefont = pygame.font.SysFont('Comic Sans MS', 30)
s = socket.socket()
port = 32477
try:
    lwhfuihworueh=connect_ip
    s.connect((connect_ip, port))
except:
    main=False
    s.connect(('127.0.0.1', port))

class Player:
    def __init__(self):
        global screensize
        self.screenSize=screensize
        self.pos=[0, 0]
        self.direction=0        #up
        self.possessions={'wood':0, 'stone':0}
        self.weapons=[]
        self.holding=0
    def move(self, mouse, dis, pic, click):
        global pos, showInventory, water, waterdimensions, islandpic
        if not click[0] and not showInventory:
            xchange=-(mouse[0]-self.screenSize[0]/2)
            ychange=-(mouse[1]-self.screenSize[1]/2)
            self.pos[0]+=xchange/30
            self.pos[1]+=ychange/30
            pixelat=tuple(islandpic.get_at((int(-self.pos[0]+self.screenSize[0]/2+3840), int(-self.pos[1]+self.screenSize[1]/2+2160))))
            if 2.35*pixelat[2]>pixelat[0]+pixelat[1]:
            #if tuple(water.get_at((int(self.pos[0]+waterdimensions[0]/2), int(self.pos[1]+waterdimensions[1]/2))))==(0, 0, 0, 255):
                self.pos[0]+=-xchange/31
                self.pos[1]+=-ychange/31
                
        else:
            xchange=0
            ychange=0
        
            
        self.pos=pos
class Background:
    def __init__(self):
        global screensize
        self.screenSize=screensize
    def display(self, dis):
        global pos, pic
        dis.blit(pic, (pos[0]-3840, pos[1]-2160))
class Mineable:
    def __init__(self, pos, pic, hardness, resource, size):
        self.pos, self.pic, self.hardness, self.size=pos, pic, hardness, size
        self.display_pos=(0, 0)
        self.resource=resource
        self.destroyedAmount=0
    def display(self):
        global screen, pos
        screen.blit(self.pic, (pos[0]-3840+self.pos[0], pos[1]-2160+self.pos[1]))
        self.display_pos=(pos[0]-3840+self.pos[0], pos[1]-2160+self.pos[1])
    def check_for_mine(self):
        global player, mousePos
        if self.display_pos[0]<mousePos[0]<self.display_pos[0]+self.size[0]:
            if self.display_pos[1]<mousePos[1]<self.display_pos[1]+self.size[1]:
                self.destroyedAmount+=1
                if self.destroyedAmount>self.hardness:
                    self.destroyedAmount=0
                    player.possessions[self.resource]+=1
class Obstacle:
    def __init__(self, pos, dire):
        self.pos=[int(pos[0]), int(pos[1])]
        self.orient=float(dire)
    def draw(self):
        global pos, screen
        dx=cos(self.orient)*100
        dy=sin(self.orient)*100
        self.display_pos=(pos[0]+self.pos[0]-3840,pos[1]+self.pos[1]-2160)
        pygame.draw.line(screen,(128, 128, 128), (self.display_pos[0]-dx, self.display_pos[1]-dx), (self.display_pos[0]+dx, self.display_pos[1]+dx))
def inventory(localplayer, pic):
    global screen
    screen.blit(pic, (160, 160))
    inventoryDisplay=myfont.render('x'+str(localplayer.possessions['wood']), False, black)
    screen.blit(inventoryDisplay, (525, 240))
    inventoryDisplay=myfont.render('x'+str(localplayer.possessions['stone']), False, black)
    screen.blit(inventoryDisplay, (825, 240))
    
pygame.init()
pos=[0, 0]
display_width = screensize[0]
display_height = screensize[1]
screen = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Attack!')
playerpygamepic=pygame.image.load('player.png')
playerpic=image.open('player.png')
waterdimensions=image.open('water.png').size

islandpic=pygame.image.load("16k island.png")
water=pygame.image.load("water.png")

treepic=pygame.image.load("tree.png")
stonepic=pygame.image.load("stone.png")

inventorypic=pygame.image.load("inventory.png")


#islandpic=water

mineables=[]
for i in range(25):
    mineables.append(Mineable((random.randint(2100, 3000), random.randint(2100, 3000)), treepic, 10, 'wood', (50, 100)))
for i in range(25):
    mineables.append(Mineable((random.randint(5000, 5800), random.randint(2000, 3000)), treepic, 10, 'wood', (50, 100)))
mineables.append(Mineable((3200, 950), stonepic, 25, 'stone', (611, 330)))
clock = pygame.time.Clock()
player=Player()
background=Background()
showInventory=0
obstacles=[]
prevright=False
obstacle_placed=False
GameRun=True
while GameRun:
    screen.fill((0, 255, 255))
    pic=islandpic
    mousePos=pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    try:
        player.direction=atan((mousePos[0]-640)/(mousePos[1]-360))*180/pi
        playerpicturned=playerpic.rotate(atan((mousePos[0]-640)/(mousePos[1]-360))*180/pi)
    except:
        if mousePos[0]<640:
            player.direction=90
            playerpicturned=playerpic.rotate(90)
        else:
            playerdirection=270
            playerpicturned=playerpic.rotate(270)
    if mousePos[1]>360:
        player.direction+=180
        playerpicturned=playerpicturned.rotate(180)
    obstacle_placed=False
    
    playerpicturned=playerpicturned.save('playertu.png')
    convertImage('playertu.png')
    playerpicdis=pygame.image.load("playertu.png")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRun = False
        if event.type == pygame.KEYDOWN:
            showInventory=1-showInventory
        if event.type==pygame.MOUSEBUTTONDOWN:
            if int(event.button)==3:
                obstacle_placed=True
    if bool(pygame.key.get_pressed()[27]):
        GameRun=False
    if bool(pygame.key.get_pressed()[44]):
        GameRun=False
    background.display(screen)
    for i in mineables:
        i.display()
    if click[0]:
        for i in mineables:
            i.check_for_mine()
    s.send(bytes((str((round(player.direction), round(pos[0]), round(pos[1]), obstacle_placed)))[1:-1], 'utf-8'))
    player.move(mousePos, screen, playerpicdis, click)
    recieve_data=ast.literal_eval(s.recv(1048576).decode())
    for i in recieve_data:
        data=recieve_data[i]
        others=playerpic.rotate(int(data[0]))
        otherplayerpicturned=others.save('playertu.png')
        convertImage('playertu.png')
        otherplayerpicdis=pygame.image.load("playertu.png")
        screen.blit(otherplayerpicdis, (int(data[1])+display_width/2-pos[0]-50, int(data[2])+display_height/2-pos[1]-50))
        if eval(data[3]):
            obstacles.append(Obstacle(data[1:3], data[0]))
    for i in obstacles:
        i.draw()
    if showInventory==1:
        inventory(player, inventorypic)
    #posdis=myfont.render('x'+str(pos), False, black)
    #screen.blit(posdis, (0, 0))
    pygame.display.flip()
    #print(clock.get_fps())
    clock.tick(30)
pygame.quit()
