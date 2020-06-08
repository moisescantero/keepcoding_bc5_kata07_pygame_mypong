import pygame as pg 
from pygame.locals import *
import sys

BACKGROUND = (0,240,0)#CONSTANTE PARA MODIFICAR COLOR DE FONDO
YELLOW = (255, 255, 0)


class Ball:
    def __init__(self):
        self.vx = 5#velocidad desplazamiento de la bola para coordenada x
        self.vy = 5#velocidad desplazamiento de la bola para coordenada y
        self.Cx = 400#coordenada inicial x para la bola
        self.Cy = 300#coordenada inicial y para la bola
        self.h = 20
        self.w = 20
        self.image = pg.Surface((20, 20))
        self.image.fill(YELLOW)

    @property
    def posx(self):
        return self.Cx - self.w // 2#para calcular el centro real
  
    @property
    def posy(self):
        return self.Cy - self.h // 2#para calcular el centro real

    def move(self, limSupX, limSupY):#método de la clase ball para mover el objeto bola
        if self.Cx >= limSupX or self.Cx <= 0:
            self.vx *= -1
            
        if self.Cy >= limSupY or self.Cy <= 0:
            self.vy *= -1

        self.Cx += self.vx#coordenada incial más velocidad x de la bola
        self.Cy += self.vy



class Game:#clase juego
    def __init__(self):#método init
        self.pantalla = pg.display.set_mode((800,600))#instanciar pantalla de 800*600
        self.pantalla.fill((BACKGROUND))#asignar color de fondo negro
        self.fondo = pg.image.load("./resources/images/fondo.jpg")
        self.pantalla.blit(self.fondo, (0 , 0))#pintar el fondo del juego
        self.ball = Ball()

        pg.display.set_caption("Pong")#asignar nombre Pong a la pantalla

    def main_loop(self):
        game_over = False#variable para salir del bucle

        while not game_over:#mientras game_over sea igual a False
            for event in pg.event.get():#para cada evento compruebas
                if event.type == QUIT:#si evento es pulsar la X de la ventana
                    game_over = True#variable contro salida de bucle es True
            

            self.pantalla.blit(self.fondo, (0 , 0))#pintar el fondo del juego
            self.pantalla.blit(self.ball.image, (self.ball.posx, self.ball.posy))#pintar la bola dando imagen, posición x y posición y

            self.ball.move(800,600)
            pg.display.flip()#pintar/actualizar pantalla


    def quit(self):
        pg.quit()#cerrar pygame
        sys.exit()#usar función salida del sistema operativo para cerrar la pantalla de juego



if __name__ == "__main__":
    pg.init()#inicializar librería pygame
    game = Game()#instanciar la clase Game y guardar en variable
    game.main_loop()#ejecutar método de clase llamado main_loop
    game.quit()#ejecutar método de clase llamado quit

