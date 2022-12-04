# Matrix libraries
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi,noop
from luma.core.render import canvas
import time
import random

global vidas

global jugX
global jugY
global disparoJugSt
global disparoJugX
global disparoJugY

global disparoEn1St
global disparoEn1X
global disparoEn1Y

global disparoEn2St
global disparoEn2X
global disparoEn2Y

global disparoEn3St
global disparoEn3X
global disparoEn3Y

global disparoEn4St
global disparoEn4X
global disparoEn4Y

global velBalasJug
global velBalasEne
global velRotaEne

global posEnemigos
global lose

global enem1St
global enem2St
global enem3St
global enem4St
global enem5St
global enem6St
global enem7St
global enem8St

global cantEnemigos

global disparosEnemigos

global timeCount
global hitEneFlag
global start


def init():
    if(start == 0):
        vidas = 3

        jugX = 4
        jugY = 0
        disparoJugSt = 0
        disparoJugX = 0
        disparoJugY = 0

        disparoEn1St = 0
        disparoEn1X = 0
        disparoEn1Y = 0

        disparoEn2St = 0
        disparoEn2X = 0
        disparoEn2Y = 0

        disparoEn3St = 0
        disparoEn3X = 0
        disparoEn3Y = 0

        disparoEn4St = 0
        disparoEn4X = 0
        disparoEn4Y = 0

        velBalasJug = 100
        velBalasEne = 200
        velRotaEne = 1000

        posEnemigos = [0, 7, 1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6, 7, 7, 7]
        lose = [7, 0]

        enem1St = 1
        enem2St = 1
        enem3St = 1
        enem4St = 1
        enem5St = 1
        enem6St = 1
        enem7St = 1
        enem8St = 1

        cantEnemigos = 8

        disparosEnemigos = 0

        timeCount = 0
        hitEneFlag = 0
        
        start = 1


def win():
    matrix.draw_point(0, 0)
    time.sleep(1000)

def gameOver():
    matrix.draw_point(7, 7)
    time.sleep(1000)

def perderVida():
    vidas = vidas-1

    if(vidas == 0):
        gameOver()
    
    jugX = 4

def rotaEne():
    if(timeCount % velRotaEne == 0):
        matrix.draw_point(4, 4)
        time.sleep(1000)
    

def movJugador():
    dir = 0
    dir =int(input("move\n"))

    if (dir == 1):
      if (jugX == 7):
        jugX = 0
      else:
        jugX = jugX+1

    elif (dir == 3):
      if (jugX == 0):
        jugX = 7
      else:
        jugX = jugX-1

    elif (dir == 2):
      if (disparoJugSt == 0):
        disparoJugador()

def disparoJugador():
    disparoJugSt = 1
    disparoJugX = jugX
    disparoJugY = 1

def disparoEnemigo():
    disparosEnemigos = disparoEn1St+disparoEn2St+disparoEn3St+disparoEn4St
    while(disparosEnemigos<4):
        if(disparoEn1St == 0):
            disparoEn1St = 1
            disparoEn1Y = 7
            disparoEn1X = random.randint(0, 7)
        if(disparoEn2St == 0):
            disparoEn2St = 1
            disparoEn2Y = 7
            disparoEn2X = random.randint(0, 7)
        if(disparoEn3St == 0):
            disparoEn3St = 1
            disparoEn3Y = 7
            disparoEn3X = random.randint(0, 7)
        if(disparoEn4St == 0):
            disparoEn4St = 1
            disparoEn4Y = 7
            disparoEn4X = random.randint(0, 7)
        disparosEnemigos = disparoEn1St+disparoEn2St+disparoEn3St+disparoEn4St


def balaJugador():
    if(timeCount % velBalasJug == 0):
        disparoJugY = disparoJugY+1

def balaEnemigo():
    if(timeCount % velBalasEne == 0):
        if(disparoEn1St == 1):
            if(disparoEn1Y == 7):
                disparoEn1St = 0
            else:
                disparoEn1Y = disparoEn1Y-1
        if(disparoEn2St == 1):
            if(disparoEn2Y == 7):
                disparoEn2St = 0
            else:
                disparoEn2Y = disparoEn2Y-1
        if(disparoEn3St == 1):
            if(disparoEn3Y == 7):
                disparoEn3St = 0
            else:
                disparoEn3Y = disparoEn3Y-1
        if(disparoEn4St == 1):
            if(disparoEn4Y == 7):
                disparoEn4St = 0
            else:
                disparoEn4Y = disparoEn4Y-1


def detectHitEne():
    if(disparoJugY == posEnemigos[1] and disparoJugX == posEnemigos[0] and hitEneFlag == 0):
        enem1St = 0
        hitEneFlag = 1
        disparoJugSt = 0
    if(disparoJugY == posEnemigos[3] and disparoJugX == posEnemigos[2] and hitEneFlag == 0):
        enem2St = 0
        hitEneFlag = 1
        disparoJugSt = 0
    if(disparoJugY == posEnemigos[5] and disparoJugX == posEnemigos[4] and hitEneFlag == 0):
        enem3St = 0
        hitEneFlag = 1
        disparoJugSt = 0
    if(disparoJugY == posEnemigos[7] and disparoJugX == posEnemigos[6] and hitEneFlag == 0):
        enem4St = 0
        hitEneFlag = 1
        disparoJugSt = 0
    if(disparoJugY == posEnemigos[9] and disparoJugX == posEnemigos[8] and hitEneFlag == 0):
        enem5St = 0
        hitEneFlag = 1
        disparoJugSt = 0
    if(disparoJugY == posEnemigos[11] and disparoJugX == posEnemigos[10] and hitEneFlag == 0):
        enem6St = 0
        hitEneFlag = 1
        disparoJugSt = 0
    if(disparoJugY == posEnemigos[13] and disparoJugX == posEnemigos[12] and hitEneFlag == 0):
        enem7St = 0
        hitEneFlag = 1
        disparoJugSt = 0
    if(disparoJugY == posEnemigos[15] and disparoJugX == posEnemigos[14] and hitEneFlag == 0):
        enem8St = 0
        hitEneFlag = 1
        disparoJugSt = 0
    hitEneFlag = 0
    cantEnemigos = cantEnemigos -1
    if(cantEnemigos == 0):
        win()


def detectHitJug():
    if(disparoEn1St == 1 and disparoEn1Y == 0):
        if(disparoEn1X == jugX):
            disparoEn1St = 0
            perderVida()
    if(disparoEn2St == 1 and disparoEn2Y == 0):
        if(disparoEn2X == jugX):
            disparoEn2St = 0
            perderVida()
    if(disparoEn3St == 1 and disparoEn3Y == 0):
        if(disparoEn3X == jugX):
            disparoEn3St = 0
            perderVida()
    if(disparoEn4St == 1 and disparoEn4Y == 0):
        if(disparoEn4X == jugX):
            disparoEn4St = 0
            perderVida()



def display():

    matrix.draw_point(jugX, jugY)

    if(enem1St == 1):
        matrix.draw_point(posEnemigos[0], posEnemigos[1])
    if(enem2St == 1):
        matrix.draw_point(posEnemigos[2], posEnemigos[3])
    if(enem3St == 1):
        matrix.draw_point(posEnemigos[4], posEnemigos[5])
    if(enem4St == 1):
        matrix.draw_point(posEnemigos[6], posEnemigos[7])
    if(enem5St == 1):
        matrix.draw_point(posEnemigos[8], posEnemigos[9])
    if(enem6St == 1):
        matrix.draw_point(posEnemigos[10], posEnemigos[11])
    if(enem7St == 1):
        matrix.draw_point(posEnemigos[12], posEnemigos[13])
    if(enem8St == 1):
        matrix.draw_point(posEnemigos[14], posEnemigos[15])

    if(disparoEn1St == 1):
        matrix.draw_point(disparoEn1X, disparoEn1Y)
    if(disparoEn2St == 1):
        matrix.draw_point(disparoEn2X, disparoEn2Y)
    if(disparoEn3St == 1):
        matrix.draw_point(disparoEn3X, disparoEn3Y)
    if(disparoEn4St == 1):
        matrix.draw_point(disparoEn4X, disparoEn4Y)

    if(disparoJugSt == 1):
        matrix.draw_point(disparoJugX, disparoJugY)
    


def main():
    matrix = Matrix()
    start = 0
    init()
    while vidas>0:
        movJugador()
        disparoJugador()
        disparoEnemigo()
        balaJugador()
        balaEnemigo()
        detectHitEne()
        detectHitJug()
        rotaEne()
        display()
        timeCount = timeCount+1
        

    #matrix.draw_point(1,0)
    #matrix.draw_point(jugX, jugY)
    #print(jugX,line)
    #time.sleep(0.1)

class Matrix(object):
  def _init_(self):
    super(Matrix, self)._init_()
    self.device = self.create_matrix_device(1, 0, 0)
  def create_matrix_device(self, n, block_orientation, rotate):
    # Create matrix device
    print("Creating device...")
    serial = spi(port = 0, device = 0, gpio = noop())
    device = max7219(serial,cascaded=n, block_orientation=block_orientation, rotate = rotate)
    print("Device created")
    return device
  def draw_point(self,x,y):
    with canvas(self.device) as draw:
      draw.point((x,y), fill="green")


if __name__=="__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass