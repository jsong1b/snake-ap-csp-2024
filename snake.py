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
    if board == None:
        usage()
        exit(3)

    exit(0)

def usage():
    print("USAGE: ./snake.py [WIDTH] [HEIGHT]")
    print("where [WIDTH] and [HEIGHT] are integers between 10 and 30")

def createBoard(width, height):
    if not 10 <= width <= 30 or not 10 <= height <= 30:
        return None

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


if __name__ == "__main__":
    main(sys.argv[1:])

# ex: set nu relativenumber list :