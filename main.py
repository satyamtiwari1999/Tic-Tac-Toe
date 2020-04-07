""" Main Game """
import pygame
import time

pygame.init()
clock = pygame.time.Clock()
# main display
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
width = 600
length = 800
screen = pygame.display.set_mode((length, width))
pygame.display.set_caption('Tic Tac Toe')

# setting the board image
board = pygame.image.load('images/finalborad.png')
zero = pygame.image.load('images/zero1.png')
cross = pygame.image.load('images/cross.png')
mesh = pygame.image.load('images/grid.png')
open = pygame.image.load('images/open.png')


def opening():
    ''' opening screen of the game '''
    screen.blit(open, (0, 0))
    screen.blit(pygame.image.load('images/play.png'), (650, 100))
    if sound:
        screen.blit(pygame.image.load('images/soundon.png'), (650, 400))
    else:
        screen.blit(pygame.image.load('images/no sound.png'), (650, 400))
    pygame.display.update()


def play_music(sound=True):
    screen.fill((255, 255, 255))
    screen.blit(open, (0, 0))
    screen.blit(pygame.image.load('images/line.png'), (610, 70))
    screen.blit(pygame.image.load('images/play.png'), (650, 100))
    if sound:
        screen.blit(pygame.image.load('images/soundon.png'), (650, 400))
        pygame.mixer.music.load('happy.mp3')
        pygame.mixer.music.play(-1)
    else:
        screen.blit(pygame.image.load('images/no sound.png'), (650, 400))
        pygame.mixer.music.stop()
    pygame.display.update()


def find_pos(a):
    """ returns the box number pressed """
    if a[0] <= 225 and a[0] >= 100 and a[1] <= 225 and a[1] >= 100:
        return (1, (100, 100))
        print('checked')
    elif a[0] <= 356 and a[0] >= 240 and a[1] <= 225 and a[1] >= 100:
        return (2, (240, 100))
        print('checked')
    elif a[0] <= 500 and a[0] >= 370 and a[1] <= 225 and a[1] >= 100:
        return (3, (370, 100))
        print('checked')
    elif a[0] <= 225 and a[0] >= 100 and a[1] <= 358 and a[1] >= 240:
        return (4, (100, 240))
        print('checked')
    elif a[0] <= 356 and a[0] >= 240 and a[1] <= 358 and a[1] >= 240:
        return (5, (240, 240))
        print('checked')
    elif a[0] <= 500 and a[0] >= 370 and a[1] <= 358 and a[1] >= 240:
        return (6, (370, 240))
        print('checked')
    elif a[0] <= 225 and a[0] >= 100 and a[1] <= 496 and a[1] >= 372:
        return (7, (100, 372))
        print('checked')
    elif a[0] <= 356 and a[0] >= 240 and a[1] <= 496 and a[1] >= 372:
        return (8, (240, 372))
        print('checked')
    elif a[0] <= 500 and a[0] >= 370 and a[1] <= 496 and a[1] >= 372:
        return (9, (370, 372))
        print('checked')
    else:
        return ('out', 'not in range')


def update_screen(moves, current, screen=screen, grid=mesh):
    # screen.blit(board, (0, 0))
    screen.fill((255, 255, 255))
    screen.blit(grid, (100, 100))
    screen.blit(pygame.image.load('images/line.png'), (610, 70))
    if current == 1:
        screen.blit(zero, (650, 100))
    else:
        screen.blit(cross, (650, 100))
    for i in moves.values():
        if i[0] == '0':
            screen.blit(zero, i[1])
        else:
            screen.blit(cross, i[1])
    pygame.display.update()


def check_winner(moves):
    to_win = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
              (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    players = {'0': [], '*': []}
    for i in moves:
        if moves[i][0] == '0':
            players['0'].append(i)
        else:
            players['*'].append(i)
    # print(players)
    for player in players:
        for elem in to_win:
            count = 0
            for j in elem:
                if j in players[player]:
                    count += 1
                else:
                    break
            if count == 3:
                return player
    if len(players['0']) + len(players['*']) == 9:
        return 'Its a Draw'


def game_loop(main_screen=screen, width=width, lenght=length, board=board):
    """ main loop of the game """
    moves = {}  # stores the moves of the player
    player = 1  # 1 for first player and 0 for the second player
    while True:
        # main_screen.blit(board, (0, 0))
        # main_screen.fill((255, 255, 255))
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # print(event.pos)
                    box, index = find_pos(event.pos)
                    # print(box)
                    if box != 'out' and box not in moves.keys():
                        if player:
                            moves[box] = ('0', index)
                            player -= 1
                            # print(moves)
                        else:
                            moves[box] = ('*', index)
                            player += 1
                            # print(moves)
            elif event.type == pygame.QUIT:
                return 0
        update_screen(moves, player)
        # checking the winner
        win = check_winner(moves)
        if win == '0':
            print('player 1 wins')
            time.sleep(2)
            break
        elif win == '*':
            print('player 2 wins')
            time.sleep(2)
            break
        elif win == 'Its a Draw':
            print('Its a Draw')
            time.sleep(2)
            break
        pygame.display.update()
        clock.tick(15)
    return 1


play_music()
sound = True
while True:
    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load('images/line.png'), (610, 70))
    opening()
    start = False
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                x, y = i.pos
                if x >= 650 and x <= 750 and y <= 200 and y >= 100:
                    start = True
                elif x >= 650 and x <= 750 and y <= 500 and y >= 400:
                    sound = False if sound else True
                    play_music(sound)
        elif i.type == pygame.QUIT:
            pygame.quit()
    if start:
        break
    clock.tick(10)


while True:
    if game_loop() == 0:
        break
    else:
        continue
pygame.quit()
