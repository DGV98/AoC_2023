import os
import sys
import re
import pprint


def parse(filepath):
    if not os.path.exists(filepath):
        sys.exit("File does not exist")
    matrix = []
    with open(filepath) as f:
        for line in f.readlines():
            line = line.strip()
            chars = []
            for char in line:
                chars.append(char)
            matrix.append(chars)
    
    return matrix


def get_num(matrix, i, j):
    width = len(matrix[0])
    num = ''
    while j < width:
        print(f"Position: {i}, {j}")
        if matrix[i][j].isdigit():
            num += matrix[i][j]
        else:
            break
        j += 1
    return num



def part_1(matrix):
    n, m = len(matrix), len(matrix[0])
    i, j = 0, 0
    positions_checked = set()
    while i < n:
        while j < m:
            char = matrix[i][j]
            if not char.isdigit() and char != ".":

        



if __name__ == "__main__":
    matrix = parse("sample.txt")
    pprint.pprint(matrix)

    print(get_num(matrix, 0, 0))
