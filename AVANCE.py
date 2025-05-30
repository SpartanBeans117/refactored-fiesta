import pygame

# Inicia el programa
pygame.init()

# Tamaño de la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título de la ventana
pygame.display.set_caption("SpartanGame")

# Definir colores
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)

# Fuente para el texto
fuente = pygame.font.Font(None, 50)

# Funciones para cada escena
def escena_inicio():
    pantalla.fill(color_negro)
    texto = "SPARTAN GAME"
    superficie_texto = fuente.render(texto, True, color_blanco)
    pantalla.blit(superficie_texto, (800 // 2 - superficie_texto.get_width() // 2, 
                                      600 // 2 - superficie_texto.get_height() // 2))

def escena_juego():
    pantalla.fill(color_negro)
    texto = "JUEGO"
    superficie_texto = fuente.render(texto, True, color_blanco)
    pantalla.blit(superficie_texto, (800 // 2 - superficie_texto.get_width() // 2, 
                                      600 // 2 - superficie_texto.get_height() // 2))

# Variable para la escena actual
escena_actual = escena_inicio

# Bucle del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                escena_actual = escena_inicio
            elif evento.key == pygame.K_RETURN:
                escena_actual = escena_juego
            
    
    # Renderizar la escena actual
    escena_actual()
    
    # Actualizador de la pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()
