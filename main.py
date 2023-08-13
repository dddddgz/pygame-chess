import pygame
from chess import *
from stockfish import Stockfish
pygame.init()

fish = Stockfish("stockfish-windows-x86-64-avx2.exe")
fish.set_depth(10)
board = Board()

screen = pygame.display.set_mode((460, 460))
bg = pygame.image.load('images/bg.png')

images = {
    (BLACK, KING)  : pygame.image.load('images/bk.png'),
    (BLACK, QUEEN) : pygame.image.load('images/bq.png'),
    (BLACK, ROOK)  : pygame.image.load('images/br.png'),
    (BLACK, KNIGHT): pygame.image.load('images/bn.png'),
    (BLACK, BISHOP): pygame.image.load('images/bb.png'),
    (BLACK, PAWN)  : pygame.image.load('images/bp.png'),
    (WHITE, KING)  : pygame.image.load('images/wk.png'),
    (WHITE, QUEEN) : pygame.image.load('images/wq.png'),
    (WHITE, ROOK)  : pygame.image.load('images/wr.png'),
    (WHITE, KNIGHT): pygame.image.load('images/wn.png'),
    (WHITE, BISHOP): pygame.image.load('images/wb.png'),
    (WHITE, PAWN)  : pygame.image.load('images/wp.png'),
}
pygame.display.set_caption("二向箔 Chess")
pygame.display.set_icon(images[(BLACK, PAWN)])

back = pygame.Surface((50, 50)).convert_alpha()
back.fill((0, 0, 0, 0))
pygame.draw.circle(back, 'BurlyWood', (20, 20), 20)

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    screen.blit(bg, (0, 0))
    for row in range(8):
        for col in range(8):
            piece = board.piece_at(square(row, col))
            if piece:
                color = piece.color
                piece_type = piece.piece_type
                image = images[(color, piece_type)]
                screen.blit(image, (30 + row * 50, 30 + col * 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
