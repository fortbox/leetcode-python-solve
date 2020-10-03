#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i, v in enumerate(nums):
            if nums.count(v) == 1:
                res.append(v)
        return res
