#!/usr/bin/env python

def read_file(filename):
    return [ line.strip() for line in open(filename) ]

def convert_lines_to_number_matrix(lines):
    return [ [ int(x) for x in line.split() ] for line in lines ]

def print_number_matrix(matrix, digit_size=1):
    for row in matrix:
        print ' '.join([ str(x).zfill(digit_size) for x in row ])

def matrix_groups_horizontal(matrix, group_size=2):
    groups = []

    length = len(matrix)
    for i in range(length):
        row = matrix[i]
        for j in range(length-(group_size-1)):
            groups.append(row[j:j+group_size])
    return groups

def matrix_groups_vertical(matrix, group_size=2):
    groups = []

    length = len(matrix)
    for i in range(length):
        for j in range(length-(group_size-1)):
            col = []
            for k in range(j, j+group_size):
                col.append(matrix[k][i])
            groups.append(col)
    return groups

def matrix_groups_diagonal_left_to_right(matrix, group_size=2):
    groups = []
    length = len(matrix)
    for i in range(length-(group_size-1)):
        for j in range(length-(group_size-1)):
            group = []
            for k in range(group_size):
                group.append(matrix[j+k][i+k])
            groups.append(group)
    return groups

def matrix_groups_diagonal_right_to_left(matrix, group_size=2):
    groups = []
    length = len(matrix)
    for i in range(length-1, group_size-2, -1):
        for j in range(length-(group_size-1)):
            group = []
            for k in range(group_size):
                group.append(matrix[i-k][j+k])
            groups.append(group)
    return groups
