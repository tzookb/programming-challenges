class Solution:
    def getPosVal(self,x , y, board: List[List[int]]) -> None:
        # beyond edges
        if x < 0 or y < 0:
            return 0
        if x >= len(board[0]) or y >= len(board):
            return 0

        curState = board[y][x]
        if curState == 1 or curState == 3:
            return 1
        if curState == 0 or curState == 2:
            return 0

    def countNeighbors(self,x , y, board: List[List[int]]) -> None:
        return sum([
            self.getPosVal(x-1, y, board),
            self.getPosVal(x-1, y-1, board),
            self.getPosVal(x, y-1, board),
            self.getPosVal(x+1, y-1, board),
            self.getPosVal(x+1, y, board),
            self.getPosVal(x+1, y+1, board),
            self.getPosVal(x, y+1, board),
            self.getPosVal(x-1, y+1, board),
        ])

    def getNextState(self,x , y, board: List[List[int]]) -> None:
        val = self.getPosVal(x, y, board)
        neighbors = self.countNeighbors(x, y, board)
        if val == 0 and neighbors == 3:
            return 2

        if val == 0:
            return 0

        if neighbors < 2 or neighbors > 3:
            return 3
        else:
            return 1

    def gameOfLife(self, board: List[List[int]]) -> None:
        for y in range(len(board)):
            for x in range(len(board[0])):
                nextState = self.getNextState(x, y, board)
                board[y][x] = nextState
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 2:
                    board[y][x] = 1
                elif board[y][x] == 3:
                    board[y][x] = 0

        return board