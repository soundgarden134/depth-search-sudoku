import numpy as np
import copy

class Sudoku:
    matrix = [[]]


    def __init__(self, mat):
        self.matrix = mat


    def is_final_state(self):
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j] == 0:
                    return False
        return True

    def check_horizontal_rows(self):
        temp_set = set()
        for i in range(9):
            temp_set.clear()
            for j in range(9):
                if self.matrix[i][j] != 0:
                    if self.matrix[i][j] in temp_set:
                        return False
                    else:
                        temp_set.add(self.matrix[i][j])

            #si temp set tiene repetidos return false

        return True;

    def check_vertical_rows(self):
        temp_set = set()
        for i in range(9):
            temp_set.clear()
            for j in range(9):
                if self.matrix[j][i] != 0:
                    if self.matrix[j][i] in temp_set:
                        return False
                    else:
                        temp_set.add(self.matrix[j][i])

            #si temp set tiene repetidos return false

        return True;

    #no mirar esta funcion, se podia hacer mejor pero no podia pensar
    def check_box(self):
        temp_set = set()
        for i in range(3):
            for j in range(3):
                if self.matrix[j][i] != 0:
                    if self.matrix[j][i] in temp_set:
                        return False
                    else:
                        temp_set.add(self.matrix[j][i])
        temp_set.clear()
        for i in range(3,6):
            for j in range(3):
                if self.matrix[j][i] != 0:
                    if self.matrix[j][i] in temp_set:
                        return False
                    else:
                        temp_set.add(self.matrix[j][i])
        temp_set.clear()
        for i in range(6,9):
            for j in range(3):
                if self.matrix[j][i] != 0:
                    if self.matrix[j][i] in temp_set:
                        return False
                    else:
                        temp_set.add(self.matrix[j][i])
        temp_set.clear()
        for i in range(3):
            for j in range(3,6):
                if self.matrix[j][i] != 0:
                    if self.matrix[j][i] in temp_set:
                        return False
                    else:
                        temp_set.add(self.matrix[j][i])
        temp_set.clear()
        for i in range(3,6):
            for j in range(3,6):
                if self.matrix[j][i] != 0:
                    if self.matrix[j][i] in temp_set:
                        return False
                    else:
                        temp_set.add(self.matrix[j][i])
        temp_set.clear()
        for i in range(6,9):
            for j in range(3,6):
                if self.matrix[j][i] != 0:
                    if self.matrix[j][i] in temp_set:
                        return False
                    else:
                        temp_set.add(self.matrix[j][i])
        temp_set.clear()
        for i in range(3):
            for j in range(6,9):
                if self.matrix[j][i] != 0:
                    if self.matrix[j][i] in temp_set:
                        return False
                    else:
                        temp_set.add(self.matrix[j][i])
        temp_set.clear()
        for i in range(3,6):
            for j in range(6,9):
                if self.matrix[j][i] != 0:
                    if self.matrix[j][i] in temp_set:
                        return False
                    else:
                        temp_set.add(self.matrix[j][i])
        temp_set.clear()
        for i in range(6,9):
            for j in range(6,9):
                if self.matrix[j][i] != 0:
                    if self.matrix[j][i] in temp_set:
                        return False
                    else:
                        temp_set.add(self.matrix[j][i])



        return True

    def is_valid(self):
        if self.check_horizontal_rows() and self.check_vertical_rows() and self.check_box():
            return True
        else:
            return False

    def print_matrix(self):  #para visualizar matriz

        print("\n\n\n\n\n")
        for i in range(len(self.matrix)):
            line = ""
            if i == 3 or i == 6:
                print("---------------------")
            for j in range(len(self.matrix[i])):
                if j == 3 or j == 6:
                    line += "| "
                line += str(self.matrix[i][j])+" "
            print(line)

