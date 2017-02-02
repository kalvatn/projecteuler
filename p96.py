from lib.util import read_file


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

assert parse_sudoku_grids()[0][0] == '003020600'

