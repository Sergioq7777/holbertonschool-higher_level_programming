#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            if i == len(matrix[j]) - 1:
                print("{}".format(matrix[j][i]), end='')
            else:
                print(matrix[j][i], end=' ')
        print()
