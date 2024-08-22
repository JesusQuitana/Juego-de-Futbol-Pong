#CURSO DE PHYTON // PYGAME // PRIMER JUEGO SENCILLO

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

#PUNTUACION
score1 = 0
score2 = 0

#FPS
fps=pygame.time.Clock()

#PANTALLA
fondo=pygame.image.load("assets/fondo.jpg")
tamaño=(1020,600)
pantalla=pygame.display.set_mode(tamaño)
ejecucionPantallaJuego=False
ejecucionPantallaMenu=True

width = fondo.get_width()
height = fondo.get_height()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('fUTBOL')

#GOL
gol = pygame.mixer.Sound('gol.wav')

#IMAGEN DE FONDO
pantalla.blit(fondo, [0,0])


#COORDENADAS Y TAMAÑO DE LAS ARQUERIAS

cord_x_arqueria_player1=15
cord_y_arqueria_player1=250

cord_x_arqueria_player2=992
cord_y_arqueria_player2=250

width_arqueria_player1=14
height_arqueria_player1=100

width_arqueria_player2=14
height_arqueria_player2=100

#COORDENADAS Y TAMAÑO DE JUGADORES

width_player=15
height_player=75

cord_x_player1=50
cord_y_player1=300-(height_player/2)

cord_x_player2=960
cord_y_player2=300-(height_player/2)

#VELOCIDADES DE LOS JUGADORES
speed_y_player1=0
speed_y_player2=0

#COORDENADAS Y TAMAÑO DE PELOTA

cord_x_pelota=320
cord_y_pelota=240
radius_pelota=10

#VELOCIDAD DE LA PELOTA
speed_x_pelota=4
speed_y_pelota=4

def texto_puntuacion(frame, text, size, x, y):
    font = pygame.font.SysFont('Small Fonts', size, bold=True)
    text_frame = font.render(text, True, NEGRO)
    text_rect = text_frame.get_rect()
    text_rect.midtop = (x,y)
    frame.blit(text_frame, text_rect)
    
#TEXTO
font_texto=pygame.font.SysFont('Courier', 30, bold=True)

def texto_inicio(text, font, colorT, cordTx, cordTy):
    img=font.render(text, True, colorT)
    pantalla.blit(img, (cordTx, cordTy))

#----------------------------------------BUCLE PRINCIPAL DEL MENNU---------------------------------------

while ejecucionPantallaMenu==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ejecucionPantallaJuego=False
            ejecucionPantallaMenu=False
            
        #INTERACCION DEL MENU
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                ejecucionPantallaJuego=True
                ejecucionPantallaMenu=False
                
            if event.key==pygame.K_ESCAPE:
                ejecucionPantallaMenu=False
                ejecucionPantallaJuego=False
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                print('Juego Ejecutado')
                
            if event.key==pygame.K_ESCAPE:
                print('Salida del Menu')
    
    #ZONA DE LOGICA
    
    #ZONA DE DIBUJO
    
    #IMAGEN DE FONDO
    pantalla.blit(fondo, [0,0])
    
    #TEXTO
    cuadro1=pygame.draw.rect(pantalla, NARANJA, (260, 370, 525, 95))
    texto_inicio('PULSA ESPACIO PARA COMENZAR', font_texto, AMARILLO, 280, 380)
    texto_inicio('Y PRESIONA "ESC" PARA SALIR', font_texto, AMARILLO, 280, 420)
    
    cuadro2=pygame.draw.rect(pantalla, NARANJA, (60, 210, 900, 90))
    texto_inicio('UTILIZA "W Y S" PARA MOVER AL JUGADOR 1', font_texto, AMARILLO, 140, 220)
    texto_inicio(' Y USA "ARRIBA Y ABAJO" PARA MOVER AL JUGADOR 2', font_texto, AMARILLO, 80, 250)
    
    #ACTUALIZACION
    pygame.display.update()
    fps.tick(60)
    
#----------------------------------------BUCLE PRINCIPAL-------------------------------------
while ejecucionPantallaJuego==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ejecucionPantallaJuego=False
    
    #ZONA LOGICA

        #JUGADOR 1
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_w:
                speed_y_player1-=3
            if event.key==pygame.K_s:
                speed_y_player1+=3
            if event.key==pygame.K_ESCAPE:
                ejecucionPantallaJuego=False
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                speed_y_player1=0
            if event.key==pygame.K_s:
                speed_y_player1=0
                
        #JUGADOR 2
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                speed_y_player2-=3
            if event.key==pygame.K_DOWN:
                speed_y_player2+=3
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                speed_y_player2=0
            if event.key==pygame.K_DOWN:
                speed_y_player2=0
                
    if cord_y_player1>495:
        cord_y_player1=495
    if cord_y_player1<30:
        cord_y_player1=30
        
    if cord_y_player2>495:
        cord_y_player2=495
    if cord_y_player2<30:
        cord_y_player2=30
    
    #ZONA LOGICA
    
    #COLOR DE LA PANTALLA
    
    pantalla.blit(fondo, [0,0])


    
    #ZONA DE DIBUJO
    
    canchaLinea1=pygame.draw.line(pantalla, BLANCO, (20,20), (1000,20), 5)
    canchaLinea2=pygame.draw.line(pantalla, BLANCO, (1000,20), (1000,580), 5)
    canchaLinea3=pygame.draw.line(pantalla, BLANCO, (1000,580), (20,580), 5)
    canchaLinea4=pygame.draw.line(pantalla, BLANCO, (20,580), (20,20), 5)
    
    arqueria_player1=pygame.draw.rect(pantalla, NEGRO, (cord_x_arqueria_player1, cord_y_arqueria_player1, width_arqueria_player1, height_arqueria_player1))
    arqueria_player2=pygame.draw.rect(pantalla, NEGRO, (cord_x_arqueria_player2, cord_y_arqueria_player2, width_arqueria_player2, height_arqueria_player2))
    
    lineaguia1=pygame.draw.line(pantalla, BLANCO, (510, 20), (510, 580), 4)
    #lineaguiah=pygame.draw.line(pantalla, BLANCO, (0, 300), (1020, 300), 4)
    lineaguia2=pygame.draw.circle(pantalla, BLANCO, (511, 311), 16)
    
    player1=pygame.draw.rect(pantalla, BLANCO, (cord_x_player1, cord_y_player1, width_player, height_player))
    cord_y_player1+=speed_y_player1
    
    player2=pygame.draw.rect(pantalla, BLANCO, (cord_x_player2, cord_y_player2, width_player, height_player))
    cord_y_player2+=speed_y_player2
    
    pelota=pygame.draw.circle(pantalla, BLANCO, (cord_x_pelota, cord_y_pelota), radius_pelota)
    
    #ZONA DE DIBUJO
    
    #COLISIONES
    if (pelota.colliderect(player1) or pelota.colliderect(player2)):
        speed_x_pelota*=-1
    
    if pelota.colliderect(canchaLinea2) or pelota.colliderect(canchaLinea4):
        speed_x_pelota*=-1
        
    if pelota.colliderect(canchaLinea1) or pelota.colliderect(canchaLinea3):
        speed_y_pelota*=-1
    
    cord_x_pelota+=speed_x_pelota
    cord_y_pelota+=speed_y_pelota
    
    if pelota.colliderect(arqueria_player1):
        score1 += 1
        speed_x_pelota*=-1
        cord_x_pelota=320
        cord_y_pelota=240
        gol.play()
        
    if pelota.colliderect(arqueria_player2):
        score2 += 1
        speed_x_pelota*=-1
        cord_x_pelota=320
        cord_y_pelota=240
        gol.play()
    
    #ACTUALIZACION
    pygame.display.update()
    fps.tick(60)
    
    texto_puntuacion(fondo, (' EQUIPO A : '+ str(score2)+'        '+' EQUIPO B : '+ str(score1)+'        '), 40, 530, 80)
    

pygame.quit()