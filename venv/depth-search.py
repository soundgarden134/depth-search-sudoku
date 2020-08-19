from classes import Sudoku
import copy
import numpy as np

matrix = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sudoku_stack = Sudoku(matrix)

stack = []
i_history = []
j_history = []
i_history.append(0)
j_history.append(2)

stack.append(sudoku_stack)

def get_sudoku(sudoku, i, j, n): #retorna un sudoku resuelto
    sudoku.matrix[i][j] = n
    return sudoku


def get_lowest_possible(sudoku, i, j):  #recibe un sudoku y retorna el menor numero posible para cambiar la posicion dada
    aux = copy.deepcopy(sudoku)
    aux.matrix[i][j] += 1
    while not aux.is_valid():
        aux.matrix[i][j] += 1
    return aux.matrix[i][j]

def next_zero_i(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku.matrix[i][j] == 0:
                return i
    return 100

def next_zero_j(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku.matrix[i][j] == 0:
                return j
    return 100

i = 0  #posicion del primer 0
j = 2

while not stack[-1].is_final_state():
    stack[-1].print_matrix()
    print(i_history)
    print(j_history)
    print(stack[-1].matrix[i][j])

    n = get_lowest_possible(stack[-1], i, j)
    if n >= 10:
        stack.pop()
        stack[-1].matrix[i][j] = 0
        i_history.pop()
        j_history.pop()
    else:
        new_sudoku = get_sudoku(stack[-1], i, j, n)
        stack.append(new_sudoku)
        i = next_zero_i(new_sudoku)
        j = next_zero_j(new_sudoku)
        i_history.append(i)
        j_history.append(j)

    i = i_history[-1]
    j = j_history[-1]



print(stack[-1].print_matrix())