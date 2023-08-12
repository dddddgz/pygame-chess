import pygame
from pprint import pprint
pygame.init()

WINDOW = 400
# 一个棋盘中有8行8列
GRID = WINDOW // 8

class Chessman(pygame.sprite.Sprite):
    def __init__(self, color, name):
        # color: b黑色 / w白色
        # name: k王 / q后 / r车 / b象 / n马 / p兵
        self.color = color
        self.name = name
        self.image = pygame.image.load(f'images/{color}{name}.png')
        self.back = pygame.Surface((GRID, GRID)).convert_alpha()
        self.back.fill((0, 0, 0, 0))
        pygame.draw.circle(self.back, 'BurlyWood', self.back.get_rect().center, GRID / 2)
        self.rect = self.image.get_rect()
        # 不显示棋子
        self.rect.topleft = (-GRID, -GRID)
        self.row = -1
        self.col = -1
        self.moved = False

    def move(self, row=None, col=None):
        # 设置棋子的位置
        # row: 行
        # col: 列
        old_row = self.row
        old_col = self.col
        if row is None:
            row = old_row
        if col is None:
            col = old_col
        self.row = row
        self.col = col
        self.rect.topleft = col * GRID, row * GRID
        if old_row != -1 and old_col != -1:
            chessboard[old_row][old_col] = None
        if self.row != -1 and self.col != -1:
            chessboard[self.row][self.col] = self

    def left(self, n=1):
        if self.col > 0:
            return chessboard[self.row][self.col - n]
    
    def right(self, n=1):
        if self.col < 7:
            return chessboard[self.row][self.col + n]
    
    def up(self, n=1):
        if self.row > 0:
            return chessboard[self.row - n][self.col]
    
    def down(self, n=1):
        if self.row < 7:
            return chessboard[self.row + n][self.col]

    def __repr__(self):
        return self.color + self.name
    
    def __str__(self):
        return f'{self.color}{self.name} {self.col, self.row}'

    def get_moves(self):
        # 获取可能的移动
        # 返回：坐标 [(row, col), ...]
        res = []
        if self.color == 'w':
            # 白
            if self.name == 'k':
                # 王
                pass
            elif self.name == 'p':
                # 兵
                if mode:
                    if self.up() is None:
                        res.append((self.col, self.row - 1))
                        if self.row == 6 and self.up(2) is None:
                            res.append((self.col, self.row - 2))
                    if self.left() and self.left().up() and self.left().color == 'b':
                        res.append((self.col - 1, self.row - 1))
                    if self.right() and self.right().up() and self.right().color == 'b':
                        res.append(self.col - 1, self.row - 1)
                else:
                    if self.down() is None:
                        res.append((self.col, self.row + 1))
                        if self.row == 1 and self.down(2) is None:
                            res.append((self.col, self.row + 2))
                    if self.left() and self.left().down() and self.left().color == 'b':
                        res.append((self.col - 1, self.row + 1))
                    if self.right() and self.right().down() and self.right().color == 'b':
                        res.append((self.col + 1, self. row + 1))
        return res

# mode: True白棋在下面 / False黑棋在下面
mode = True

def place_chess():
    # 生成棋子 Chessman 对象
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
        if mode:
            chessman.move(row=7)
        else:
            chessman.move(row=0)
        if chessman.color == 'w':
            # 白
            if chessman.name == 'k':
                # 王
                chessman.move(col=4)
            elif chessman.name == 'q':
                # 后
                chessman.move(col=3)
            elif chessman.name == 'r':
                # 车
                if wr:
                    chessman.move(col=7)
                else:
                    chessman.move(col=0)
                    wr = True
            elif chessman.name == 'b':
                # 象
                if wb:
                    chessman.move(col=5)
                else:
                    chessman.move(col=2)
                    wb = True
            elif chessman.name == 'n':
                # 马
                if wn:
                    chessman.move(col=6)
                else:
                    chessman.move(col=1)
                    wn = True
            elif chessman.name == 'p':
                # 兵
                if mode:
                    chessman.move(row=6)
                else:
                    chessman.move(row=1)
                chessman.move(col=wp)
                wp += 1
        elif chessman.color == 'b':
            # 黑
            if mode:
                chessman.move(row=0)
            else:
                chessman.move(row=7)
            if chessman.name == 'k':
                # 王
                chessman.move(col=4)
            elif chessman.name == 'q':
                # 后
                chessman.move(col=3)
            elif chessman.name == 'r':
                # 车
                if br:
                    chessman.move(col=7)
                else:
                    chessman.move(col=0)
                    br = True
            elif chessman.name == 'b':
                # 象
                if bb:
                    chessman.move(col=5)
                else:
                    chessman.move(col=2)
                    bb = True
            elif chessman.name == 'n':
                # 马
                if bn:
                    chessman.move(col=6)
                else:
                    chessman.move(col=1)
                    bn = True
            elif chessman.name == 'p':
                # 白兵
                if mode:
                    chessman.move(row=1)
                else:
                    chessman.move(row=6)
                chessman.move(col=bp)
                bp += 1
        chessboard[chessman.row][chessman.col] = chessman

def print_chessboard():
    # 调试用的函数，用于输出 chessboard
    pprint(chessboard)

def pos_to_grid(pos):
    # 将 (x, y) 转换为 (row, col)
    # pos: 坐标 (x, y)
    x, y = pos
    row, col = y // GRID, x // GRID
    return row, col

screen = pygame.display.set_mode((WINDOW, WINDOW))
bg = pygame.image.load('images/bg.png')
pygame.display.set_caption('二向箔 Chess')
pygame.display.set_icon(bg)
chessboard = []
place_chess()

chosen = None
clock = pygame.time.Clock()
down = False
running = True
while running:
    clock.tick(30)
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            down = True
            # 是否找到点击的棋子
            found = False
            for row in chessboard:
                for chessman in row:
                    if chessman and chessman.rect.collidepoint(event.pos):
                        chosen = chessman
                        found = True
                        break
            if not found:
                chosen = None
        elif event.type == pygame.MOUSEBUTTONUP:
            down = False
            row, col = pos_to_grid(event.pos)
            print(chosen.get_moves(), (row, col))
            if chosen and (row, col) in chosen.get_moves():
                chosen.rect.topleft = (col * GRID, row * GRID)
            else:
                chosen.move()
        elif event.type == pygame.MOUSEMOTION:
            if chosen and down:
                chosen.rect.center = event.pos
    for row in chessboard:
        for chessman in row:
            if chessman:
                if chessman is chosen:
                    screen.blit(chessman.back, chessman.rect)
                    for pos in chessman.get_moves():
                        screen.blit(chessman.back, (pos[0] * GRID, pos[1] * GRID))
                screen.blit(chessman.image, chessman.rect)
    pygame.display.flip()
pygame.quit()
