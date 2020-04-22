import time
from random import randint
from copy import deepcopy


DIMENSIONS = {'x': 50, 'y':50}
NEIGHBOURS = ((-1, 00), (1, 00),
              (-1, -1), (00, -1),
              (1, -1), (-1, 1),
              (00, 1), (1, 1))
WORLD = [[]]


def seed():
    """initial seed of the game"""
    global WORLD
    for x in range(DIMENSIONS['x']):
        WORLD.append([])
        for _ in range(DIMENSIONS['y']):
            WORLD[x].append(int(randint(0, 100) / 90))
    #WORLD = [[0,0,0,0,0],
    #         [0,1,0,0,0],
    #         [0,0,1,1,0],
    #         [0,1,1,0,0],
    #         [0,0,0,0,0]]

def evolve():
    """evolve the world"""
    global WORLD
    next_world = deepcopy(WORLD)
    for x in range(DIMENSIONS['x']):
        for y in range(DIMENSIONS['y']):
            lives = 0
            for iv in range(x-1, x+2):
                for jv in range(y-1, y+2):
                    if iv == x and jv == y:
                        continue
                    xx = (iv) % DIMENSIONS['x']
                    yy = (jv) % DIMENSIONS['y']
                    lives += WORLD[xx][yy]
            next_world[x][y] = is_alive(lives, WORLD[x][y])
    WORLD = next_world


def is_alive(lives, current):
    """see if the cell will be alive in the next world"""
    if lives == 3:
        return 1
    if lives > 3 or lives < 2:
        return 0
    return current



def draw():
    """draw the array"""
    # Clear the screen:
    print('\033c')
    for x in range(DIMENSIONS['x']):
        for y in range(DIMENSIONS['y']):
            char = '⬜'
            if WORLD[x][y]:
                char = '⬛'
            print(char, end = '')
        print()
    time.sleep(1)


def main():
    """main"""
    seed()
    while True:
        draw()
        evolve()

if __name__ == "__main__":
    main()
