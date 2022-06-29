from typing import List
class Solution:
    def genKey(self, row, col) -> str:
        return "%s_%s" % (row, col)
        

    def extractFromKey(self, key):
        res = key.split("_")
        return ( int(res[0]), int(res[1]) )


    def isOverBorder(self, row, col, board) -> bool:
        if row < 0 or row >= len(board):
            return True
        if col < 0 or col >= len(board[0]):
            return True
        return False

    def explore(self, start_row, start_col, board):
        in_island = {}
        is_visited = {}
        to_explore = [(start_row, start_col)]
        while to_explore:
            row, col = to_explore.pop()
            
            if self.isOverBorder(row, col, board):
                return [False, in_island]

            cur = board[row][col]
            key = self.genKey(row, col)
            if key in is_visited:
                continue
            is_visited[key] = True
            if cur == "O":
                in_island[key] = True
                to_explore.append((row+1, col))
                to_explore.append((row-1, col))
                to_explore.append((row, col+1))
                to_explore.append((row, col-1))
                continue
            if cur == "X":
                continue
            
        return [True, in_island]


    def changeIslandCells(self, board: List[List[str]], island):
        for item in island:
            row, col = self.extractFromKey(item)
            board[row][col] = "X"

    def solve(self, board: List[List[str]]) -> None:
        visited = {}
        for row in range(len(board)):
            for col in range(len(board[0])):
                key = self.genKey(row, col)
                if key in visited:
                    continue
                cur = board[row][col]
                if cur == "X":
                    continue
                is_island, island = self.explore(row, col, board)
                if is_island:
                    self.changeIslandCells(board, island)
                else:
                    visited = {**island, **visited}




board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

s = Solution()
res = s.solve(board)
print(board)