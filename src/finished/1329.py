#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        column = len(mat[0])
        for i in range(-row + 1, column - 1):
            q = []
            for j in range(row):
                for k in range(column):
                    if k - j == i:
                        q.append(mat[j][k])
            q.sort(reverse=True)
            # q.sort()
            for j in range(row):
                for k in range(column):
                    if k - j == i:
                        mat[j][k] = q.pop()
        return mat


if __name__ == '__main__':
    mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
    solution = Solution()
    res = solution.diagonalSort(mat)
    print(res)
