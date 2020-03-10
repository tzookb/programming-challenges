
def gridChallenge(grid):
    for idx, row in enumerate(grid):
        chars = list(row)
        chars.sort()
        grid[idx] = "".join(chars)
    
    for colidx in range(len(grid[0])):
        minval = 0
        for rowidx in range(len(grid)):
            curChar = grid[rowidx][colidx]
            curCharVal = ord(curChar)
            if curCharVal < minval:
                return "NO"
            minval = curCharVal
    return "YES"

k = 3 
contests = [
    'mpxz',
    'abcd',
    'wlmf',
]

# 29
print(gridChallenge(contests))