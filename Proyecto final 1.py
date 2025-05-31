import pygame
import random

# Inicia el programa
pygame.init()

# Tamaño de la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo de la ventana
pygame.display.set_caption("BeanRunner")

# Definir colores
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)

# Fuente para el texto
fuente = pygame.font.Font(None, 50)

# Personaje
P1 = pygame.Rect(50, 200, 50, 50)
gravity = 1
jump = -15
velocity = 0
ground = 200

# Enemigo
enemigos = []
speed = 10

# Generar enemigo
GENERAR_ENEMIGO = pygame.USEREVENT + 1
pygame.time.set_timer(GENERAR_ENEMIGO, 1500)

# Funciones para cada escena
def escena_inicio():
    pantalla.fill(color_negro)
    texto = "Presiona [Enter]"
    superficie_texto = fuente.render(texto, True, color_blanco)
    pantalla.blit(superficie_texto, (800 // 2 - superficie_texto.get_width() // 2, 
                                      600 // 2 - superficie_texto.get_height() // 2))

def escena_juego():
    global velocity
    pantalla.fill(color_blanco)

    # Gravedad
    velocity += gravity
    P1.y += velocity
    if P1.y >= ground:
        P1.y = ground
        
    # Dibujar Personaje
    pygame.draw.rect(pantalla, color_negro, P1)

    # Mover enemigo
    for enemigo in enemigos:
        enemigo["rect"].x -= enemigo["speed"]
        pygame.draw.rect(pantalla, color_negro, enemigo["rect"])

# Variable para la escena actual
escena_actual = escena_inicio

# Bucle del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and P1.y == ground:
                velocity = jump
            if evento.key == pygame.K_ESCAPE:
                escena_actual = escena_inicio
            elif evento.key == pygame.K_RETURN:
                escena_actual = escena_juego
        elif evento.type == GENERAR_ENEMIGO:
            if escena_actual == escena_juego:
                velocidad_nueva = speed + len(enemigos)
                enemigos.append({"rect": pygame.Rect(700, ground, 20, 50), "speed": velocidad_nueva})
    
    # Renderizar la escena actual
    escena_actual()

    # Colision
    for enemigo in enemigos:
        if P1.colliderect(enemigo["rect"]):
            enemigos.clear()
            P1.x = 50
            P1.y = ground
            velocity = 0
            escena_actual = escena_inicio

    # Actualizador de la pantalla
    pygame.display.flip()
    pygame.time.delay(30)

# Salir del juego
pygame.quit()
