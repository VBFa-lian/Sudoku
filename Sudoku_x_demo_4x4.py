# didn't sure if we need a class or not
import random
import sys

import numpy as np

import dancing_link_3x3


def matrix_index_formula(i, j, k):
    """
    Use the indices of sudoku and value of each cell to get the index of col number of that binary matrix, we may use
    later on the exact-cover algorithm
    :param i: the row index of sudoku
    :param j: the col index of sudoku
    :param k: the number we fill in the cell of sudoku
    :return: a tuple of indices that refer to our 4 restriction
    """
    a = i * 4 + j
    b = i * 4 + 15 + k
    c = j * 4 + k + 31
    d = (i//2*2 + j//2)*4 + k + 47

    return a, b, c, d


# for the sudoku initialization
def sudoku_init(initial_numbers):
    # dic is to store the (i,j,k)
    sudoku_dic = {}
    restriction = set()
    while len(sudoku_dic) < initial_numbers:
        # get random rows
        i = random.randint(0,3)
        # get random columns
        j = random.randint(0, 3)
        # fill with 1-9
        fill_in_num = [ 1, 2, 3, 4]
        k = random.choice(fill_in_num)
        # check if (i, j) is already in the dic
        # if in, next round
        if (i, j) in sudoku_dic:
            continue
        # call the formula function to check if the restriction repeat or not
        a, b, c, d = matrix_index_formula(i, j, k)
        if a in restriction or b in restriction or c in restriction:
            continue
        else:
            restriction.update((a, b, c, d))
            sudoku_dic[(i, j)] = k
    return sudoku_dic


def generate_sudoku_matrix(sudoku_dic):
    """
   We use this function to initialize matrix
   First, we sure that we have 324 cols:
        4*81 = 324
        Cause, we have 4 restrictions:
        1. each cell of sudoku must have a number (a)
        2. each row of sudoku must not have the same number (b)
        3. each column of sudoku must not have the same number (c)
        4. each 3*3 grid must not have the same number (d)
        As we need to fill in 81 cells, we need to determine whether these 81 cells meet with these 4 restrictions,
        that is to determine 4*81 YES/NO (1 or 0), so we need to raise a binary matrix with 324 cols. We determine our
        dancing linked list have 324 heads
    Then, we try to infer our rows number:
        We initialize our sudoku with 11 numbers and all the other 81-11 = 70 cells are empty. For each empty cell, we
        the maximum hypothesis as 9 possible numbers to fill in (1-9), than we have 70*90 = 630 possibilities. Also, we
        already have 11 numbers, which are fixed. So overall we will have 630 + 11 = 641 rows
    Thus, we have the binary matrix that is [641(rows) x 342(cols)]
    :param sudoku_dic:
    :return: sudoku_matrix
   """
    sudoku_matrix = dancing_link_3x3.DancingLinks(64, 64)
    for i in range(4):
        for j in range(4):
            # if the location already has the number
            if (i, j) in sudoku_dic:
                k = sudoku_dic[(i, j)]
                a, b, c, d = matrix_index_formula(i, j, k)
                # we get the matrix's row index from the following formula
                row_index = (i * 4 + j) * 4 + k - 1
                # use the dancing link method append row
                dancing_link_3x3.DancingLinks.append_row(sudoku_matrix, [a, b, c, d], row_index)
            # if the location do not have number yet
            else:
                # fill in with 1-9
                for k in range(1,5):
                    # do the same thing as above
                    a, b, c, d = matrix_index_formula(i, j, k)
                    row_index = (i * 4 + j) * 4 + k - 1
                    dancing_link_3x3.DancingLinks.append_row(sudoku_matrix, [a, b, c, d], row_index)
    return sudoku_matrix


def print_init(dic):
    rows = cols = 4
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    for (i, j), k in dic.items():
        board[i][j] = k
    for row in board:
        print(row)


init_numbers = 0
dic = sudoku_init(init_numbers)

matrix = generate_sudoku_matrix(dic)


def print_answer(sudoku):
    rows = cols = 4
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    for (i, j), k in dic.items():
        board[i][j] = k
    for row in board:
        print(row)

#print(matrix.to_array())
ans = []
sudoku = dancing_link_3x3.DancingLinks.dancing(matrix, ans)
print(matrix.dancing(ans))

print(ans)

#matrix.to_array()
#np.set_printoptions(threshold=np.inf)
#print(matrix.to_array())
#file1 = open("matrix.txt", "w")
#file1.write(str(matrix.to_array()))