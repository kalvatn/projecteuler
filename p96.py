from lib.util import read_file


""" grids[0]
0 0 3 | 0 2 0 | 6 0 0|
9 0 0 | 3 0 5 | 0 0 1|
0 0 1 | 8 0 6 | 4 0 0|
_____________________|
0 0 8 | 1 0 2 | 9 0 0|
7 0 0 | 0 0 0 | 0 0 8|
0 0 6 | 7 0 8 | 2 0 0|
_____________________|
0 0 2 | 6 0 9 | 5 0 0|
8 0 0 | 2 0 3 | 0 0 9|
0 0 5 | 0 1 0 | 3 0 0|
"""

def parse_sudoku_grids():
    grids = []
    grid = None
    for line in read_file('p96.txt'):
        if line.startswith('Grid'):
            if grid is not None:
                grids.append(grid)
            grid = []
        else:
            grid.append(line)
    grids.append(grid)

    # for grid in grids:
    #     print grid
    #     for row in grid:
    #         print row
    return grids

class Sudoku(object):
    def __init__(self, grid):
        self.grid = grid
        self.cells = []

        for i in range(1, 10):
            c = []
            cy = 0
            cx = 0
            if i in [1, 2, 3]:
                cy = 0
                cx = i - 1
            if i in [4, 5, 6]:
                cy = 3
                cx = i - 4
            if i in [7, 8, 9]:
                cy = 6
                cx = i - 7
            c = []
            cx *= 3
            # print i, cx, cx+3, cy, cy+3
            for row in self.grid[cy:cy+3]:
                c.append(row[cx:cx+3])
            self.cells.append(c)

    def cell(self, n):
        return self.cells[n-1]

    def update_cell(self, n, y, x, value):

        if n in [1, 2, 3]:
            gy = 0
            gx = n - 1
        if n in [4, 5, 6]:
            gy = 3
            gx = n - 4
        if n in [7, 8, 9]:
            gy = 6
            gx = n - 7
        gx *= 3
        gx += (x)
        gy += (y)
        # print n, y, x, gy, gx
        cell = self.cells[n-1]
        cell_row = cell[y-1]
        current_value = cell_row[x-1]

        if current_value == '0':
            if value not in self.row_missing(gy):
                print '%s not in row missing %s' % (value, self.row_missing(gy))
            if value not in self.col_missing(gx):
                print '%s not in col missing %s' % (value, self.col_missing(gx))
            tmp = list(cell_row)
            tmp[x-1] = value
            self.cells[n-1][y-1] = ''.join(tmp)

    def row(self, n):
        return self.grid[n-1]

    def col(self, n):
        col = []
        for row in self.grid:
            col.append(row[n-1])
        return ''.join(col)

    def missing(self, part):
        missing = []
        for x in '123456789':
            if x not in part:
                missing.append(x)
        return ''.join(sorted(missing))


    def col_missing(self, n):
        col = self.col(n)
        return self.missing(col)

    def row_missing(self, n):
        row = self.row(n)
        return self.missing(row)

    def cell_missing(self, n):
        cell = ''.join(self.cell(n))
        return self.missing(cell)



grids = parse_sudoku_grids()
assert grids[0][0] == '003020600'

s = Sudoku(grids[0])
print s.cell_missing(1)
assert s.cell_missing(1) == '245678'
assert s.cell_missing(2) == '1479'
assert s.cell_missing(3) == '235789'
assert s.cell_missing(4) == '123459'
assert s.cell_missing(5) == '34569'
assert s.cell_missing(6) == '134567'
assert s.cell_missing(7) == '134679'
assert s.cell_missing(8) == '4578'
assert s.cell_missing(9) == '124678'

assert s.row_missing(1) == '145789'
assert s.row_missing(2) == '24678'
assert s.row_missing(3) == '23579'
assert s.row_missing(4) == '34567'
assert s.row_missing(5) == '1234569'
assert s.row_missing(6) == '13459'
assert s.row_missing(7) == '13478'
assert s.row_missing(8) == '14567'
assert s.row_missing(9) == '246789'

assert s.col_missing(1) == '123456'
assert s.col_missing(2) == '123456789'
assert s.col_missing(3) == '479'
assert s.col_missing(4) == '459'
assert s.col_missing(5) == '3456789'
assert s.col_missing(6) == '147'
assert s.col_missing(7) == '178'
assert s.col_missing(8) == '123456789'
assert s.col_missing(9) == '234567'

for i in range(1, 10):
    print '%d - cell %s, missing : %9s' % (i, s.cell(i), s.cell_missing(i))

for i in range(1, 10):
    print '%d - row  %s, missing : %9s' % (i, s.row(i), s.row_missing(i))

for i in range(1, 10):
    print '%d - col  %s, missing : %9s' % (i, s.col(i), s.col_missing(i))


s.update_cell(1, 1, 1, '2')
# print s.cell(1)
assert s.cell(1) == ['203', '900', '001' ]

print s.cell(5)
s.update_cell(5, 1, 2, '3')
assert s.cell(5) == ['132', '000', '708' ]
print s.cell(5)

print s.cell(9)
s.update_cell(9, 2, 2, '4')
assert s.cell(9) == ['500', '049', '300' ]
