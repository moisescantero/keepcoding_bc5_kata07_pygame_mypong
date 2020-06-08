import pygame#importar librería pygame
from pygame.locals import *
import sys#librería funcionalidades del sistema operativo

pygame.init()#iniciar librería

pantalla = pygame.display.set_mode((600,400))#asignar a variable pantalla de 600*400
pygame.display.set_caption("Hola mundo")#nombrar la pantalla como Hola mundo

rojo = 0
direccion = 1#dirección para saber si subimos valor de color rojo o bajamos
juego_activo = True

while True:
    for event in pygame.event.get():#comprobamos eventos y pasamos
        if event.type == QUIT:#si el evento es pulsar la X de la ventana
            juego_activo = False#condición para salir del bucle

    if rojo >= 255:#si rojo es mayor de 255
        direccion = -1#la dirección es descendente (disminuimos valor del color rojo)
    
    if rojo <= 0:#si rojo es menor de 0 
        direccion = 1 #la dirección es ascendente (aumentamos valor del color rojo)

    rojo += direccion#valor de rojo es igual a su valor + el de dirección

    pantalla.fill((rojo,0,0))#color pantalla todo rojo
    pygame.display.flip()#actualizar/pintar la pantalla
    pygame.time.delay(10)#retraso de 5 segundos y se cierra la pantalla
    


pygame.quit()#cierra pygame
sys.exit()#usar salida del sistema operativo para cerrar ventana



