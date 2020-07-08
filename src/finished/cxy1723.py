#  Copyright (c) 2020
#  @Author: xiaoweixiang
from collections import defaultdict
from typing import List


class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        """
        只想到了暴利
        :param matrix:
        :return:
        """
        if not matrix: return []
        mxrow = defaultdict(int)
        mxcol = defaultdict(int)
        rows, cols = len(matrix), len(matrix[0])
        res = []
        for r in range(rows)[::-1]:
            for c in range(cols)[::-1]:
                if matrix[r][c] == 0:
                    mxrow[r, c] = 1 + mxrow[r, c + 1]
                    mxcol[r, c] = 1 + mxcol[r + 1, c]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    maxsize = min(mxrow[r, c], mxcol[r, c])
                    cursize = 0 if not res else res[2]
                    for size in range(maxsize, cursize, -1):
                        if mxcol[r, c + size - 1] >= size and mxrow[r + size - 1, c] >= size:
                            res = [r, c, size]
                            break
        return res
