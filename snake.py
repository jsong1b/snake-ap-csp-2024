#!/usr/bin/env python

import curses
import sys

##################
# INITIALIZATION #
##################

def main(argv):
    if not len(argv) == 2:
        usage()
        exit(1)

    width = 0
    height = 0
    try:
        width = int(argv[0])
        height = int(argv[1])
    except:
        usage()
        exit(2)

    board = createBoard(width, height)
    if board == False:
        usage()
        exit(3)

    curses.wrapper(snake, board)

    exit(0)

def usage():
    print("USAGE: ./snake.py [HEIGHT] [WIDTH]")
    print("where [HEIGHT] and [WIDTH] are integers between 10 and 50")

def createBoard(width, height):
    if not 10 <= width <= 50 or not 10 <= height <= 50:
        return False

    board = []
    for i in range(height + 2):
        board.append([])
        for j in range(width + 2):
            if i == 0 or i == height + 1:
                board[i].append("=")
            elif j == 0 or j == width + 1:
                board[i].append("|")
            else:
                board[i].append("0")

    board[0][0] = "+"
    board[height + 1][0] = "+"
    board[0][width + 1] = "+"
    board[height + 1][width + 1] = "+"

    return board


##################
# GAME FUNCTIONS #
##################


def snake(stdscr, board):
    height = len(board)
    width = len(board[0])

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    curses.curs_set(False)

    snake = []
    for i in range(3):
        snake.append((height // 2, (width // 4) - i))
    fruit = ((height // 2), width - (width // 4))

    drawScreen(board, snake, fruit, stdscr)

    stdscr.getstr()


def drawScreen(board, snake, fruit, stdscr):
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[i]):
            if board[i][j] == "0":
                continue
            stdscr.addstr(i, j, board[i][j])

    for i, pos in enumerate(snake):
        stdscr.addstr(pos[0], pos[1], "O", curses.color_pair(1) | curses.A_DIM)
        if i == 0:
            stdscr.addstr(pos[0], pos[1], "O", curses.color_pair(1) | curses.A_BOLD)

    stdscr.addstr(fruit[0], fruit[1], "X", curses.color_pair(2) | curses.A_BOLD)

    stdscr.refresh()


###########
# STARTUP #
###########

if __name__ == "__main__":
    main(sys.argv[1:])

# ex: set nu relativenumber list :