#!/usr/bin/env python

import curses
import sys


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
    print("where [HEIGHT] and [WIDTH] are integers between 10 and 30")

def createBoard(width, height):
    if not 10 <= width <= 30 or not 10 <= height <= 30:
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


def snake(stdscr, board):
    height = len(board)
    width = len(board[0])

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)


    curses.curs_set(False)

    snake = [(height // 2, width // 4), (height // 2, (width // 4) - 1)]
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
        stdscr.addstr(pos[0], pos[1], "O")
        if i == 0:
            stdscr.addstr(pos[0], pos[1], "O", curses.color_pair(1))

    stdscr.addstr(fruit[0], fruit[1], "X")

    stdscr.refresh()


if __name__ == "__main__":
    main(sys.argv[1:])

# ex: set nu relativenumber list :