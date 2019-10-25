import sys
import pygame
import stdio

run = True
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 128)

pygame.init()
window = pygame.display.set_mode((900,800))
pygame.display.set_caption("Chessboard")

dimensions_of_board = 8
square = 80
window.fill(white)

spot = 0
for i in range(1, dimensions_of_board + 1):
	for j in range(1, dimensions_of_board + 1):
		if spot % 2 == 0:
			pygame.draw.rect(window, white, [square * j, square * i, square, square])
		else:
			pygame.draw.rect(window, black, [square * j, square * i, square, square])
		spot += 1
	spot -= 1
pygame.draw.rect(window, black, [square, square, dimensions_of_board*square, dimensions_of_board*square],  1)

pygame.display.update()

font = pygame.font.Font('freesansbold.ttf', 45)
text = font.render('A    B    C    D    E    F    G    H', True, blue, white)
window.blit(text, [93, 30])

font2 = pygame.font.Font('freesansbold.ttf', 50)
text2 = font2.render('1    2    3    4    5    6    7    8', True, blue, white)
text2 = pygame.transform.rotate(text2, 90)
window.blit(text2, [20, 95])


pygame.display.update()


while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
