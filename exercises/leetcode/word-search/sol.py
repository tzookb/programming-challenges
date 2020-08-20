from typing import List

class Solution(object):
    def exist(self, board, word):
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.visited = {}
        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtrack(row, col, word):
                    return True
        return False

    def backtrack(self, row, col, remainder):
        if len(remainder) == 0:
            return True
        if row < 0 or row == self.rows or col < 0 or col == self.cols:
            return False
        visitedKey = str(row) + "_" + str(col)
        if visitedKey in self.visited:
            return False
        if self.board[row][col] != remainder[0]:
            return False

        ret = False
        # marking the cur as we dont want to backtrack a visited cell
        self.visited[visitedKey] = True
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, remainder[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret:
                return True

        # revert the change, a clean slate and no side-effect
        del self.visited[visitedKey]

        # Tried all directions, and did not find any match
        return ret



board = [
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
]
word = "ABCESEEEFS"
sol = Solution()
res = sol.exist(board, word)
print(res)
