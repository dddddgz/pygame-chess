import pygame
from chess import *
from stockfish import Stockfish
pygame.init()

def square_to_pos(square):
    row, col = square
    x = 30 + col * 50
    y = 30 + row * 50
    return (x, y)

def pos_to_square(pos):
    x, y = pos
    row = (y - 30) // 50
    col = (x - 30) // 50
    return (row, col)

engine = Stockfish("stockfish-windows-x86-64-avx2.exe")
engine.set_depth(10)
board = Board()

screen = pygame.display.set_mode((460, 460))
bg = pygame.image.load('images/bg.png')

images = {
    (WHITE, KING)  : pygame.image.load('images/wk.png'),
    (WHITE, QUEEN) : pygame.image.load('images/wq.png'),
    (WHITE, ROOK)  : pygame.image.load('images/wr.png'),
    (WHITE, KNIGHT): pygame.image.load('images/wn.png'),
    (WHITE, BISHOP): pygame.image.load('images/wb.png'),
    (WHITE, PAWN)  : pygame.image.load('images/wp.png'),
    (BLACK, KING)  : pygame.image.load('images/bk.png'),
    (BLACK, QUEEN) : pygame.image.load('images/bq.png'),
    (BLACK, ROOK)  : pygame.image.load('images/br.png'),
    (BLACK, KNIGHT): pygame.image.load('images/bn.png'),
    (BLACK, BISHOP): pygame.image.load('images/bb.png'),
    (BLACK, PAWN)  : pygame.image.load('images/bp.png'),
}
pygame.display.set_caption('二向箔 Chess')
pygame.display.set_icon(images[(BLACK, PAWN)])

back = pygame.Surface((50, 50)).convert_alpha()
back.fill((0, 0, 0, 0))
pygame.draw.circle(back, 'BurlyWood', (25, 25), 25)

clock = pygame.time.Clock()
chosen = None
running = True
while running:
    clock.tick(50)
    screen.fill((0, 0, 0))
    screen.blit(bg, (30, 30))
    if chosen:
        screen.blit(back, square_to_pos(chosen))
        moves = list(map(str, board.legal_moves))
        for move in moves:
            if move[:2] == 'abcdefgh'[chosen[1]] + '87654321'[chosen[0]]:
                screen.blit(back, square_to_pos(('87654321'.index(move[3]), ('abcdefgh'.index(move[2])))))
    for col in range(8):
        for row in range(8):
            piece = board.piece_at(square(col, row))
            if piece:
                color = not piece.color
                piece_type = piece.piece_type
                image = images[(color, piece_type)]
                screen.blit(image, square_to_pos((row, col)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row, col = pos_to_square(event.pos)
            if 0 <= row < 8 and 0 <= col < 8 and board.piece_at(square(col, row)):
                chosen = (row, col)
            else:
                chosen = None
    pygame.display.flip()
pygame.quit()
