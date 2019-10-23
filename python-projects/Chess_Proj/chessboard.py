import sys
import pygame
import stdio

run = True
white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((900,800))
pygame.display.set_caption("Chessboard")

boardLength = 8
size = 80
window.fill(white)

x = 0
for i in range(1, boardLength + 1):
    for j in range(1, boardLength + 1):
        if x % 2 == 0:
            pygame.draw.rect(window, white,[size*j, size*i, size, size])
        else:
            pygame.draw.rect(window, black, [size*j, size*i, size, size])
        x+=1
    x-=1
pygame.draw.rect(window, black, [size, size, boardLength*size, boardLength*size], 1)

pygame.display.update()

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
