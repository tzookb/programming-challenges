class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        rounds = size // 2
        steps = size - 1
        for round_idx in range(rounds):
            for step in range(steps):
                cur_top = matrix[round_idx][step]
                cur_right = matrix[step][size - 1 - round_idx]
                cur_bottom = matrix[size - 1 - round_idx][size - 1 - step]
                cur_left = matrix[size - 1 - step][round_idx]
                
                matrix[round_idx][step] = cur_left
                matrix[step][size - 1 - round_idx] = cur_top
                matrix[size - 1 - round_idx][size - 1 - step] = cur_right
                matrix[size - 1 - step][round_idx] = cur_bottom

            steps -= 2