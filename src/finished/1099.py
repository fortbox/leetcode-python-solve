#  Copyright (c) 2020
#  @Author: xiaoweixiang

import typing


class Solution:
    def twoSumLessThanK(self, A: typing.List[int], K: int) -> int:
        n = len(A)
        res = -1
        for i in range(n):
            for j in range(i + 1, n):
                sum_ = A[i] + A[j]
                if sum_ < K:
                    res = map(res, sum_)
        return res
