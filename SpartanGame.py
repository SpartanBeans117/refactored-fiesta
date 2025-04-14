import pygame

# Inicia el programa
pygame.init()

# Tamaño de la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título de la ventana
pygame.display.set_caption("SpartanGame")

# Texto de inicio
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)
fuente = pygame.font.Font(None, 50)

# Crea el texto
texto = "SPARTAN GAME"
superficie_texto = fuente.render(texto, True, color_blanco)
posicion_texto = (800 // 2 - superficie_texto.get_width() // 2, 600 // 2 - superficie_texto.get_height() // 2)

# Bucle del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    # Para que aparezca el fondo y texto
    pantalla.fill(color_negro)
    pantalla.blit(superficie_texto, posicion_texto)
    
    # Actualizador de la pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()
