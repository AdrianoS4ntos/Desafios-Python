# Desafio 21 - Reproduz um arquivo de áudio utilizando um módulo do Python.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('Desafio-021/samurai.mp3')
pygame.mixer.music.play()

input('precione enter para sair')
