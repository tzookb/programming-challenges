from typing import List
import pytest

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i in range(len(box)):
            row = box[i]
            box[i] = self.dropTo(row)
        
        return self.rotate_mat_90_deg(box)

    def dropTo(self, arr: List[int]) -> None:
        drop_to_idx = None

        for i in range(len(arr) - 1, -1, -1):
            cur = arr[i]
            if cur == ".":
                if drop_to_idx is None:
                    drop_to_idx = i
            elif cur == "*":
                drop_to_idx = None
            else: # #
                if drop_to_idx is None:
                    continue
                arr[drop_to_idx] = "#"
                arr[i] = "."
                drop_to_idx -= 1

        return arr

    def rotate_mat_90_deg(self, mat) :
        rows = len(mat)
        cols = len(mat[0])

        new_mat = [] 
        for c in range(cols):
            new_row = []
            for r in range(rows):
                cur = mat[r][c]
                new_row.insert(0, cur)
            new_mat.append(new_row)

        return new_mat


s = Solution()
arr = s.rotateTheBox([
    ["#",".","*","."],
    ["#","#","*","."]
])
# arr = s.dropTo(["#","#","."])
# print(arr)
def test_full():
    arr = ["#","#"]
    expected = ["#","#"]
    assert s.dropTo(arr) == expected
def test_free_fall():
    arr = ["#", "#", ".", ".", ".", ".", "."]
    expected = [".",".",".",".",".","#","#"]
    assert s.dropTo(arr) == expected

def test_free_fall_with_space():
    arr = ["#", ".", ".", "#", ".", ".", "."]
    expected = [".",".",".",".",".","#","#"]
    assert s.dropTo(arr) == expected

def test_fall_to_obstacle():
    arr = ["#", ".", ".", "*", ".", ".", "."]
    expected = [".",".","#","*",".",".","."]
    assert s.dropTo(arr) == expected


def test_fall_to_obstacle_and_more():
    arr = ["#", ".", "*", ".", "#", ".", "."]
    expected = [".","#","*",".",".",".","#"]
    assert s.dropTo(arr) == expected

# pytest.main()