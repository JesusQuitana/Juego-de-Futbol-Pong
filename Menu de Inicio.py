#MENU DE INICIO DEL JUEGO

import pygame, sys, random

pygame.init()

#PALETA DE COLORES
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
AMARILLO=(255,255,0)
NARANJA=(255,128,0)
MORADO=(127,0,255)
AQUA=(0,255,255)

#FPS
fps=pygame.time.Clock()

#PANTALLA
fondo=pygame.image.load("assets/imgmenu.png")
tamaño=(1020,600)
pantalla=pygame.display.set_mode(tamaño)
pantalla.blit(fondo, tamaño)
ejecucionMenu=True

#TEXTO
font_texto=pygame.font.SysFont('Courier', 30, bold=True)

def texto_inicio(text, font, colorT, cordTx, cordTy):
    img=font.render(text, True, colorT)
    pantalla.blit(img, (cordTx, cordTy))

#------------------------BUCLE PRINCIPAL DEL JUEGO------------------------------

while ejecucionMenu==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ejecucionMenu=False
            
        
        #INTERACCION DEL MENU
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                print('HOLSAAAAAAAAA')
                
            if event.key==pygame.K_ESCAPE:
                print('SALIRRRRRRRRRRRRR')
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                print('HOLKJKSAKJSJK')
                
            if event.key==pygame.K_ESCAPE:
                print('SALIRRRRRRRFGGFRRRRRR')
    
    #ZONA DE LOGICA
    
    #ZONA DE DIBUJO
    
    #IMAGEN DE FONDO
    pantalla.blit(fondo, [0,0])
    
    #TEXTO
    cuadro1=pygame.draw.rect(pantalla, NARANJA, (260, 370, 525, 95))
    texto_inicio('PULSA ESPACIO PARA COMENZAR', font_texto, AMARILLO, 280, 380)
    texto_inicio('Y PRESIONA "ESC" PARA SALIR', font_texto, AMARILLO, 280, 420)
    
    #ACTUALIZACION
    pygame.display.update()
    fps.tick(60)

pygame.quit()