#  Copyright (c) 2020
#  @Author: xiaoweixiang
import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        for left in range(col):
            _sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]
                arr = [0]
                cur = 0
                for tmp in _sum:
                    '''
                    为何用二分呢?
                    '''
                    cur += tmp
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):
                        res = max(cur - arr[loc], res)
                    bisect.insort(arr, cur)
        return res
