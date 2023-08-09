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

    @property
    def left(self):
        return chessboard[self.row][self.col - 1]

    @property
    def right(self):
        return chessboard[self.row][self.col + 1]
    
    @property
    def up(self):
        return chessboard[self.row - 1][self.col]
    
    @property
    def down(self):
        return chessboard[self.row + 1][self.col]

    def __repr__(self):
        return self.color + self.name
    
    def __str__(self):
        return f'{self.color}{self.name} {self.col, self.row}'

    def get_moves(self):
        # 获取可能的移动
        # 返回：坐标 [(row, col), ...]
        res = []
        return res

def place_chess(mode=True):
    # 生成棋子 Chessman 对象
    # mode: True白棋在下面 / False黑棋在下面
    # 重置棋盘
    chessboard.clear()
    for _ in range(8):
        chessboard.append([None for _ in range(8)])
    templist = []
    for color in 'bw':
        for name in 'kqrrbbnnpppppppp':
            chessman = Chessman(color, name)
            templist.append(chessman)
    # 车 后 象（白）
    wr = wn = wb = False
    # 车 后 象（黑）
    br = bn = bb = False
    # 白兵出现的次数
    wp = 0
    # 黑兵出现的次数
    bp = 0
    for chessman in templist:
        # 白
        if mode:
            chessman.row = 7
        else:
            chessman.row = 0
        if chessman.color == 'w':
            if chessman.name == 'k':
                # 王
                chessman.col = 4
            elif chessman.name == 'q':
                # 后
                chessman.col = 3
            elif chessman.name == 'r':
                # 车
                if wr:
                    chessman.col = 7
                else:
                    chessman.col = 0
                    wr = True
            elif chessman.name == 'b':
                # 象
                if wb:
                    chessman.col = 5
                else:
                    chessman.col = 2
                    wb = True
            elif chessman.name == 'n':
                # 马
                if wn:
                    chessman.col = 6
                else:
                    chessman.col = 1
                    wn = True
            elif chessman.name == 'p':
                # 兵
                if mode:
                    chessman.row = 6
                else:
                    chessman.row = 1
                chessman.col = wp
                wp += 1
        # 黑
        elif chessman.color == 'b':
            if mode:
                chessman.row = 0
            else:
                chessman.row = 7
            if chessman.name == 'k':
                # 王
                chessman.col = 4
            elif chessman.name == 'q':
                # 后
                chessman.col = 3
            elif chessman.name == 'r':
                # 车
                if br:
                    chessman.col = 7
                else:
                    chessman.col = 0
                    br = True
            elif chessman.name == 'b':
                # 象
                if bb:
                    chessman.col = 5
                else:
                    chessman.col = 2
                    bb = True
            elif chessman.name == 'n':
                # 马
                if wn:
                    chessman.col = 6
                else:
                    chessman.col = 1
                    wn = True
            elif chessman.name == 'p':
                # 白兵
                if mode:
                    chessman.row = 1
                else:
                    chessman.row = 6
                chessman.col = bp
                bp += 1
        chessboard[chessman.row][chessman.col] = chessman

def print_chessboard():
    # 调试用的函数，用于输出 chessboard
    for row in chessboard:
        print('[', end='')
        for chessman in row:
            print(repr(chessman).center(4), end=', ')
        print(']')

screen = pygame.display.set_mode((WINDOW, WINDOW))
chessboard = []

place_chess()
print_chessboard()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
