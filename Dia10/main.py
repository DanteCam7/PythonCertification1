import pygame
import random

# Inicializar pygame
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

# Variables del Jugador
img_jugador = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0

# Variables del Enemigo
img_enemigo = pygame.image.load('enemigo.png')
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.1
enemigo_y_cambio = 25

# Variables de la bala
img_bala = pygame.image.load('bullet.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.2
bala_visible = False


# Funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Funcion enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x+16, y+10))


# Loop del juego
se_ejecuta = True
while se_ejecuta:

    # RGB PANTALLA
    pantalla.blit(fondo, (0, 0))

    # iterar eventos
    for evento in pygame.event.get():

        # evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.2
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.2
            if evento.key == pygame.K_SPACE:
                disparar_bala(jugador_x, bala_y)

        # evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # modificar ubicación del jugador
    jugador_x += jugador_x_cambio

    # mantener dentro de bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # modificar ubicación del enemigo
    enemigo_x += enemigo_x_cambio

    # mantener dentro de bordes al enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.1
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.1
        enemigo_y += enemigo_y_cambio

    # movimiento bala
    if bala_visible:
        disparar_bala(jugador_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # actualizar
    pygame.display.update()


