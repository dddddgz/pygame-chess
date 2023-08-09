import pygame
pygame.init()

WINDOW = 640
# 一个棋盘中有8行8列
GRID = WINDOW // 8

class Chessman(pygame.sprite.Sprite):
    def __init__(self, color, name):
        # color: b黑色 / w白色
        # name: k王 / q后 / r车 / b象 / n马 / p兵
        # row for y, col for x
        self.color = color
        self.name = name
        self.image = pygame.image.load('images/' + color + name + '.png')
        self.rect = self.image.get_rect()
        # 不显示棋子
        self.rect.topleft = (-GRID, -GRID)
        self._row = -1
        self._col = -1

    @property
    def row(self):
        return self._row
    
    @row.setter
    def row(self, row):
        self._row = row
        self.rect.top = row * GRID

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, col):
        self._col = col
        self.rect.left = col * GRID

def place_chess(mode):
    # 生成棋子 Chessman 对象
    # mode: True白棋在下面 / False黑棋在下面
    chessboard.clear()
    templist = []
    for color in 'bw':
        for name in 'kqrrbbnnpppppppp':
            chessman = Chessman(color, name)
            templist.append(chessman)
    wr, wn, wb = False, False, False
    for chessman in templist:
        if chessman.color == 'w':
            if chessman.name == 'k':
                chessman.col = 4
                if mode:
                    chessman.row = 7
                else:
                    chessman.row = 0
            elif chessman.name == 'q':
                chessman.col = 3
                if mode:
                    chessman.row = 7
                else:
                    chessman.row = 0
            elif chessman.name == 'r':
                pass
                
screen = pygame.display.set_mode((WINDOW, WINDOW))
chessboard = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

