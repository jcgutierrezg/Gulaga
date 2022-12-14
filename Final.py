# Matrix libraries
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi,noop
from luma.core.render import canvas
import time
import random
#import getch
#from pynput import keyboard
#import pygame
import threading

class KeyboardThread(threading.Thread):

    def __init__(self, input_cbk = None, name='keyboard-input-thread'):
        self.input_cbk = input_cbk
        super(KeyboardThread, self).__init__(name=name)
        self.start()

    def run(self):
        while True:
            self.input_cbk(input()) #waits to get input + Return



# def my_callback(inp):
#     #evaluate the keyboard input
#     print('You Entered:', inp, ' Counter is at:')

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

velBalasJug = 10
velBalasEne = 20
velRotaEne = 100

pattern = 0

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

timeCount = 1
hitEneFlag = 0
hitJugFlag = 0

win = 0
gameOver = 0


def perderVida():
    global vidas, jugX, gameOver, disparoEn1St, disparoEn2St, disparoEn3St, disparoEn4St
    vidas = vidas-1
    disparoEn1St = 0
    disparoEn2St = 0
    disparoEn3St = 0
    disparoEn4St = 0

    if(vidas == 0):
        gameOver = 1
    
    jugX = 4

def rotaEne():
    global timeCount, velRotaEne, posEnemigos, pattern
    if(timeCount % velRotaEne == 0):
        if(pattern == 0):
            posEnemigos = [0, 6, 1, 7, 2, 6, 3, 7, 4, 6, 5, 7, 6, 6, 7, 7]
            pattern = pattern+1
        elif(pattern == 1):
            posEnemigos = [0, 7, 1, 7, 0, 6, 1, 6, 7, 7, 6, 7, 7, 6, 6, 6]
            pattern = pattern+1
        elif(pattern == 2):
            posEnemigos = [2, 7, 3, 7, 4, 7, 5, 7, 2, 6, 3, 6, 4, 6, 5, 6]
            pattern = pattern+1
        elif(pattern == 3):
            posEnemigos = [0, 7, 1, 7, 2, 6, 3, 6, 4, 6, 5, 6, 6, 7, 7, 7]
            pattern = 0
    

def movJugador(dir):
    global jugX, jugY, disparoJugSt
    #dir = 0
    #dir =int(input("move\n"))
    #dir = getch.getch()
    #events = pygame.event.get()

    # for event in events:
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_a:
    #             if (jugX == 7):
    #                 jugX = 0
    #             else:
    #                 jugX = jugX+1
    #                 print("a")
    #         if event.key == pygame.K_d:
    #             if (jugX == 0):
    #                 jugX = 7
    #             else:
    #                 jugX = jugX-1
    #                 print("d")
    #         if event.key == pygame.K_s:
    #             if (disparoJugSt == 0):
    #                 disparoJugador()
    #                 print("s")


    if (dir == 'a'):
      if (jugX == 7):
        jugX = 0
      else:
        jugX = jugX+1
        print("a")

    elif (dir == 'd'):
      if (jugX == 0):
        jugX = 7
      else:
        jugX = jugX-1
      print("d")

    elif (dir == 's'):
      if (disparoJugSt == 0):
        disparoJugador()
      print("s")
    #print("f")

def disparoJugador():
    global jugX, disparoJugSt, disparoJugX, disparoJugY
    disparoJugSt = 1
    disparoJugX = jugX
    disparoJugY = 1

def disparoEnemigo():
    global disparoEn1St, disparoEn1X, disparoEn1Y, disparoEn2St, disparoEn2X, disparoEn2Y, disparoEn3St, disparoEn3X, disparoEn3Y, disparoEn4St, disparoEn4X, disparoEn4Y, disparosEnemigos
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
    global timeCount, velBalasJug, disparoJugY, disparoJugSt
    if(timeCount % velBalasJug == 0):
        if(disparoJugSt == 1):
            if(disparoJugY == 7):
                disparoJugSt = 0
            else:
                disparoJugY = disparoJugY+1

def balaEnemigo():
    global timeCount, velBalasEne, disparoEn1St, disparoEn1Y, disparoEn2St, disparoEn2Y, disparoEn3St, disparoEn3Y, disparoEn4St, disparoEn4Y
    if(timeCount % velBalasEne == 0):
        if(disparoEn1St == 1):
            if(disparoEn1Y == 0):
                disparoEn1St = 0
            else:
                disparoEn1Y = disparoEn1Y-1
        if(disparoEn2St == 1):
            if(disparoEn2Y == 0):
                disparoEn2St = 0
            else:
                disparoEn2Y = disparoEn2Y-1
        if(disparoEn3St == 1):
            if(disparoEn3Y == 0):
                disparoEn3St = 0
            else:
                disparoEn3Y = disparoEn3Y-1
        if(disparoEn4St == 1):
            if(disparoEn4Y == 0):
                disparoEn4St = 0
            else:
                disparoEn4Y = disparoEn4Y-1


def detectHitEne():
    global disparoJugY, disparoJugX, posEnemigos, hitEneFlag, cantEnemigos, enem1St, enem2St, enem3St, enem4St, enem5St, enem6St, enem7St, enem8St, disparoJugSt, win
    if(disparoJugSt == 1):
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
        
        if(hitEneFlag == 1):
            cantEnemigos = cantEnemigos -1
        hitEneFlag = 0
        if(cantEnemigos == 0):
            win = 1


def detectHitJug():
    global jugX, disparoEn1St, disparoEn1Y, disparoEn2St, disparoEn2Y, disparoEn3St, disparoEn3Y, disparoEn4St, disparoEn4Y, hitJugFlag
    if(disparoEn1St == 1 and disparoEn1Y == 0 and hitJugFlag == 0):
        if(disparoEn1X == jugX):
            disparoEn1St = 0
            hitJugFlag = 1
            perderVida()
    if(disparoEn2St == 1 and disparoEn2Y == 0 and hitJugFlag == 0):
        if(disparoEn2X == jugX):
            disparoEn2St = 0
            hitJugFlag = 1
            perderVida()
    if(disparoEn3St == 1 and disparoEn3Y == 0 and hitJugFlag == 0):
        if(disparoEn3X == jugX):
            disparoEn3St = 0
            hitJugFlag = 1
            perderVida()
    if(disparoEn4St == 1 and disparoEn4Y == 0 and hitJugFlag == 0):
        if(disparoEn4X == jugX):
            disparoEn4St = 0
            hitJugFlag = 1
            perderVida()
    hitJugFlag = 0


def main():
    global vidas, timeCount, posEnemigos, enem1St, enem2St, enem3St, enem4St, enem5St, enem6St, enem7St, enem8St, disparoEn1St, disparoEn1X, disparoEn1Y, disparoEn2St, disparoEn2X, disparoEn2Y, disparoEn3St, disparoEn3X, disparoEn3Y, disparoEn4St, disparoEn4X, disparoEn4Y, disparoJugX, disparoJugY, cantEnemigos
    matrix = Matrix()
    #listener = keyboard.Listener(
    #on_press=on_press,
    #on_release=on_release)
    #listener.start()
    kthread = KeyboardThread(movJugador)

    while (gameOver==0 and win == 0):
        #movJugador()
        disparoEnemigo()
        balaJugador()
        balaEnemigo()
        detectHitEne()
        detectHitJug()
        rotaEne()

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

        matrix.draw_point(jugX, jugY)

        timeCount = timeCount+1
        #print(cantEnemigos)
    if(win == 1):
        print("Winner winner chicken dinner!")
    elif(gameOver == 1):
        print("Los caminos de la vida no son lo que yo esperaba")
        

    #matrix.draw_point(1,0)
    #matrix.draw_point(jugX, jugY)
    #print(jugX,line)
    #time.sleep(0.1)

class Matrix(object):
  def __init__(self):
    super(Matrix, self).__init__()
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