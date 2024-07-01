#import pygame
#pygame.init()
#pygame.mixer.music.load('desafiospython/desafio021.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()

import pygame
pygame.init()

# Verifique o caminho do arquivo
file_path = 'desafiospython/desafio021.mp3'

try:
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    # Esperar até a música terminar de tocar
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
except pygame.error as e:
    print(f"Erro ao tocar o arquivo de áudio: {e}")