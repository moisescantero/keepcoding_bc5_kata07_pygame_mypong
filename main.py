import pygame as pg 
from pygame.locals import *
import sys

BACKGROUND = (0,180,0)#CONSTANTE PARA MODIFICAR COLOR DE FONDO

class Game:#clase juego
    def __init__(self):#método init
        self.pantalla = pg.display.set_mode((800,600))#instanciar pantalla de 800*600
        self.pantalla.fill((BACKGROUND))#asignar color de fondo negro
        pg.display.set_caption("Pong")#asignar nombre Pong a la pantalla

    def main_loop(self):
        game_over = False#variable para salir del bucle

        while not game_over:#mientras game_over sea igual a False
            for event in pg.event.get():#para cada evento compruebas
                if event.type == QUIT:#si evento es pulsar la X de la ventana
                    game_over = True#variable contro salida de bucle es True
            
            pg.display.flip()#pintar/actualizar pantalla


    def quit(self):
        pg.quit()#cerrar pygame
        sys.exit()#usar función salida del sistema operativo para cerrar la pantalla de juego



if __name__ == "__main__":
    pg.init()#inicializar librería pygame
    game = Game()#instanciar la clase Game y guardar en variable
    game.main_loop()#ejecutar método de clase llamado main_loop
    game.quit()#ejecutar método de clase llamado quit

