import pygame as pg 
from pygame.locals import *
import sys
import random

BACKGROUND = (0,240,0)#CONSTANTE PARA MODIFICAR COLOR DE FONDO
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
WIN_GAME_SCORE = 3

class Ball:
    def __init__(self):
        self.vx = 5#velocidad desplazamiento de la bola para coordenada x
        self.vy = 5#velocidad desplazamiento de la bola para coordenada y
        self.Cx = 400#coordenada inicial x para la bola
        self.Cy = 300#coordenada inicial y para la bola
        self.h = 20
        self.w = 20
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(YELLOW)
        self.ping = pg.mixer.Sound("./resources/sounds/ping.wav")
        self.lost_point = pg.mixer.Sound("./resources/sounds/lost-point.wav")


    @property
    def posx(self):
        return self.Cx - self.w // 2#para calcular el centro real
  
    @property
    def posy(self):
        return self.Cy - self.h // 2#para calcular el centro real

    def move(self, limSupX, limSupY):#método de la clase ball para mover el objeto bola
        if self.Cx >= limSupX or self.Cx <= 0:
            self.vx = 0
            self.vy = 0
            self.lost_point.play()
            
        if self.Cy >= limSupY or self.Cy <= 0:
            self.vy *= -1
            self.ping.play()

        self.Cx += self.vx#coordenada incial más velocidad x de la bola
        self.Cy += self.vy

    def comprobarChoque(self, something):
        dx = abs(self.Cx - something.Cx)
        dy = abs(self.Cy - something.Cy)

        if dx < (self.w +  something.w) // 2 and dy < (self.h + something.h) // 2:
            self.vx *= -1 
            self.Cx += self.vx#coordenada incial más velocidad x de la bola
            self.Cy += self.vy     
            self.ping.play()

    def reset(self):
        self.vx = random.choice([-5 , 5])#velocidad desplazamiento de la bola para coordenada x
        self.vy = random.choice([-5 , 5])#velocidad desplazamiento de la bola para coordenada y
        self.Cx = 400#coordenada inicial x para la bola
        self.Cy = 300#coordenada inicial y para la bola
             




class Raquet:
    def __init__(self, Cx):
        self.vx = 0#velocidad desplazamiento de la bola para coordenada x
        self.vy = 5#velocidad desplazamiento de la bola para coordenada y
        self.w = 25
        self.h = 100
        self.Cx = Cx#coordenada inicial x para la bola
        self.Cy = 300#coordenada inicial x para la bola

        
        self.image = pg.Surface((self.w, self.h))
        self.image.fill((255,255,255))

    @property
    def posx(self):
        return self.Cx - self.w // 2#para calcular el centro real
  
    @property
    def posy(self):
        return self.Cy - self.h // 2#para calcular el centro real

    def move(self, limSupX, limSupY):
        self.Cx += self.vx
        self.Cy += self.vy

        #version genis
        if self.Cy < self.h // 2:
            self.Cy = self.h // 2

        if self.Cy >= limSupY - self.h // 2:
            self.Cy = limSupY - self.h // 2
        

class Game:#clase juego
    def __init__(self):#método init
        self.pantalla = pg.display.set_mode((800,600))#instanciar pantalla de 800*600
        self.pantalla.fill((BACKGROUND))#asignar color de fondo negro
        self.fondo = pg.image.load("./resources/images/fondo.jpg")
        self.pantalla.blit(self.fondo, (0 , 0))#pintar el fondo del juego
        self.ball = Ball()
        self.playerOne = Raquet(30)
        self.playerTwo = Raquet(770)
        self.status = "partida"


        self.font = pg.font.Font("./resources/fonts/font.ttf", 40)
        self.fontGrande = pg.font.Font("./resources/fonts/font.ttf", 60)

        self.marcadorOne = self.font.render("0", True, WHITE)
        self.marcadorTwo = self.font.render("0", True, WHITE)

        self.text_game_over = self.fontGrande.render("GAME OVER", True, YELLOW)
        self.text_insert_coin = self.font.render("<SPACE> - Inicio partida", True, WHITE )

        self.scoreOne = 0
        self.scoreTwo = 0

        pg.display.set_caption("Pong")#asignar nombre Pong a la pantalla



    def handleEvent(self):
        for event in pg.event.get():#para cada evento compruebas
            if event.type == QUIT:#si evento es pulsar la X de la ventana
                self.quit()
            """
            if event.type == KEYDOWN:
                if event.key == K_w:
                    self.playerOne.vy = -5
                if event.key == K_z:
                    self.playerOne.vy = 5
            """
            key_pressed = pg.key.get_pressed()
            if key_pressed[K_w]:
                self.playerOne.vy = -5
            elif key_pressed[K_z]:
                self.playerOne.vy = 5
            else:
                self.playerOne.vy = 0

            if key_pressed[K_UP]:
                self.playerTwo.vy = -5
            elif key_pressed[K_DOWN]:
                self.playerTwo.vy = 5
            else:
                self.playerTwo.vy = 0

            return False

    def bucle_partida(self):
        game_over = False
        self.scoreOne = 0
        self.scoreTwo = 0
        self.marcadorOne = self.font.render(str(self.scoreOne), True, WHITE)
        self.marcadorTwo = self.font.render(str(self.scoreTwo), True, WHITE)

        while not game_over:
            game_over = self.handleEvent()

            self.ball.move(800, 600)
            self.playerOne.move(800, 600)
            self.playerTwo.move(800, 600)
            self.ball.comprobarChoque(self.playerOne)
            self.ball.comprobarChoque(self.playerTwo)

            if self.ball.vx == 0 and self.ball.vy == 0:
                if self.ball.Cx >= 800:
                    self.scoreOne += 1
                    self.marcadorOne = self.font.render(str(self.scoreOne), True, WHITE)
                if self.ball.Cx <= 0:
                    self.scoreTwo += 1
                    self.marcadorTwo = self.font.render(str(self.scoreTwo), True, WHITE)

                if self.scoreOne == WIN_GAME_SCORE or self.scoreTwo == WIN_GAME_SCORE:
                    game_over = True

                self.ball.reset()


            self.pantalla.blit(self.fondo, (0 , 0))#pintar el fondo del juego
            self.pantalla.blit(self.ball.image, (self.ball.posx, self.ball.posy))#pintar la bola dando imagen, posición x y posición y
            self.pantalla.blit(self.playerOne.image, (self.playerOne.posx, self.playerOne.posy))#pintar raqueta player one
            self.pantalla.blit(self.playerTwo.image, (self.playerTwo.posx, self.playerTwo.posy))#pintar raqueta player two
            self.pantalla.blit(self.marcadorOne, (20, 10))
            self.pantalla.blit(self.marcadorTwo, (760, 10))
            pg.display.flip()#pintar/actualizar pantalla

        self.status = "Inicio"

    def bucle_inicio(self):
        inicio_partida = False
        while not inicio_partida:
            for event in pg.event.get():#para cada evento compruebas
                if event.type == QUIT:#si evento es pulsar la X de la ventana
                    self.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        inicio_partida = True                   
        
            self.pantalla.fill((0,0,255))
            self.pantalla.blit(self.text_game_over, (100, 100))
            self.pantalla.blit(self.text_insert_coin, (100, 200))
            
            pg.display.flip()#pintar/actualizar pantalla

        self.status = "Partida"

    def main_loop(self):

        while True:#mientras game_over sea igual a True
            if self.status == "Partida":#si estamos en partida vamos a bucle partida
                self.bucle_partida()
            else:
                self.bucle_inicio()

           

    def quit(self):
        pg.quit()#cerrar pygame
        sys.exit()#usar función salida del sistema operativo para cerrar la pantalla de juego



if __name__ == "__main__":
    pg.init()#inicializar librería pygame
    game = Game()#instanciar la clase Game y guardar en variable
    game.main_loop()#ejecutar método de clase llamado main_loop
    game.quit()#ejecutar método de clase llamado quit

