def validateSeqIsValid(row):
    numsDict = {}
    for item in row:
        if item == '.':
            continue
        if item in numsDict:
            raise "error"
        numsDict[item] = True

def validateRows(grid):
    for row in grid:
        validateSeqIsValid(row)

def validateColumns(grid):
    for col in zip(*grid):
        validateSeqIsValid(col)

def getSqaureByIdx(grid, idx):
    if idx == 0:
        x = 0
        y = 0
    elif idx == 1:
        x = 3
        y = 0
    elif idx == 2:
        x = 6
        y = 0
    elif idx == 3:
        x = 0
        y = 3
    elif idx == 4:
        x = 3
        y = 3
    elif idx == 5:
        x = 6
        y = 3
    elif idx == 6:
        x = 0
        y = 6
    elif idx == 7:
        x = 3
        y = 6
    elif idx == 8:
        x = 6
        y = 6
    return [
        grid[y][x],
        grid[y][x+1],
        grid[y][x+2],
        grid[y+1][x],
        grid[y+1][x+1],
        grid[y+1][x+2],
        grid[y+2][x],
        grid[y+2][x+1],
        grid[y+2][x+2],
    ]

def validateSqaures(grid):
    for x in range(0, 9):
        validateSeqIsValid(
            getSqaureByIdx(grid, x)
        )

def add(a,b):
    return a+b

def sudoku2(grid):
    try:
        validateRows(grid)
        validateColumns(grid)
        validateSqaures(grid)
        return True
    except:
        return False

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

res = sudoku2(grid)
print(res)