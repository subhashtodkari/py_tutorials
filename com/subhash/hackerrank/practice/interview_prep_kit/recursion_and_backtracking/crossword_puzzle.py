#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

'''
Input 	   		Output

++++++++++ 		++++++++++
+------+++ 		+POLAND+++
+++-++++++ 		+++H++++++
+++-++++++ 		+++A++++++
+++-----++ 		+++SPAIN++
+++-++-+++ 		+++A++N+++
++++++-+++ 		++++++D+++
++++++-+++ 		++++++I+++
++++++-+++ 		++++++A+++
++++++++++ 		++++++++++
POLAND;LHASA;SPAIN;INDIAancd
'''


def print_crossword_2d(crossword: List[List[str]]):
    for _ in crossword:
        print(_)
    print()


def solve_crossword(crossword: List[List[str]], words: List[str]):

    word = words.pop()
    original_word = ""
    # check rows - horizontal
    print(">>> processing word: ", word)
    print_crossword_2d(crossword)
    print("word: ", word, " horizontally")
    i = 0
    while i < 10:
        start = None
        j = 0
        while j < 10:
            print("row: ", i, ", col: ", j)
            if crossword[i][j] != '+':
                if start is None:
                    start = j
                if crossword[i][j] != '-':
                    if crossword[i][j] != word[j - start]:
                        # it is not correct word
                        # skip to next position
                        while j < 10 and crossword[i][j] != '+':
                            j += 1
                        start = None
                        continue
            if start is not None and (crossword[i][j] == '+' or j == 9):
                end = j + (1 if j == 9 and crossword[i][j] != '+' else 0)
                length = end - start
                if length == len(word):
                    # now it is possible match
                    original_word = ""
                    print("filling word: ", word)
                    for k in range(start, end):
                        original_word += crossword[i][k]
                        crossword[i][k] = word[k - start]
                    print_crossword_2d(crossword)
                    if len(words) == 0:
                        # we are done
                        return
                    # check next word
                    solve_crossword(crossword, words)
                    if len(words) != 0:
                        # it did not work out, revert position and try next
                        print("reverting word: ", word)
                        for k in range(start, end):
                            crossword[i][k] = original_word[k - start]
                        print_crossword_2d(crossword)
                    else:
                        return
                start = None
            j += 1
        i += 1
    print("after horizontal processing")
    print_crossword_2d(crossword)
    print("word: ", word, " vertically")
    # if len(words) != 0:
    # check cols - horizontal
    j = 0
    while j < 10:
        start = None
        i = 0
        while i < 10:
            print("row: ", i, ", col: ", j)
            if crossword[i][j] != '+':
                if start is None:
                    start = i
                if crossword[i][j] != '-':
                    if crossword[i][j] != word[i - start]:
                        # it is not correct word
                        while i < 10 and crossword[i][j] != '+':
                            i += 1
                        start = None
                        continue
            if start is not None and (crossword[i][j] == '+' or i == 9):
                end = i + (1 if i == 9 and crossword[i][j] != '+' else 0)
                length = end - start
                if length == len(word):
                    # now it is possible match
                    original_word = ""
                    print("filling word: ", word)
                    for k in range(start, end):
                        original_word += crossword[k][j]
                        crossword[k][j] = word[k - start]
                    print_crossword_2d(crossword)
                    if len(words) == 0:
                        # we are done
                        return
                    # check next word
                    solve_crossword(crossword, words)
                    if len(words) != 0:
                        # it did not work out, revert position and try next
                        print("reverting back word: ", word)
                        for k in range(start, end):
                            crossword[k][j] = original_word[k - start]
                        print_crossword_2d(crossword)
                    else:
                        return
                start = None
            i += 1
        j += 1
    print("after vertical processing")
    print_crossword_2d(crossword)
    if len(words) != 0:
        print("!!! adding word back: ", word)
        words.append(word)

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words: str):
    cw = [[None for x in range(10)] for y in range(10)]
    for r in range(10):
        for c in range(10):
            cw[r][c] = crossword[r][c]
    solve_crossword(cw, words.split(";"))
    # print()
    # print("crossword puzzle solved !!!!!!!!!!!!!!!!")
    # print()
    cw_str = []
    for r in cw:
        cw_str.append("".join(r))
    # for r in cw_str:
        # print(r)

    # print("returning....")

    return cw_str


if __name__ == '__main__':

    crossword1 = [
        '++++++++++',
        '+------+++',
        '+++-++++++',
        '+++-++++++',
        '+++-----++',
        '+++-++-+++',
        '++++++-+++',
        '++++++-+++',
        '++++++-+++',
        '++++++++++'
    ]

    words1 = "POLAND;LHASA;SPAIN;INDIA"

    crossword2 = [
        '+-++++++++',
        '+-++++++++',
        '+-++++++++',
        '+-----++++',
        '+-+++-++++',
        '+-+++-++++',
        '+++++-++++',
        '++------++',
        '+++++-++++',
        '+++++-++++'
    ]
    words2 = "LONDON;DELHI;ICELAND;ANKARA"

    crossword = [
        '++++++-+++',
        '++------++',
        '++++++-+++',
        '++++++-+++',
        '+++------+',
        '++++++-+-+',
        '++++++-+-+',
        '++++++++-+',
        '++++++++-+',
        '++++++++-+'
    ]
    words = "ICELAND;MEXICO;PANAMA;ALMATY"

    result = crosswordPuzzle(crossword, words)

    if result:
        for r in result:
            print(r)
