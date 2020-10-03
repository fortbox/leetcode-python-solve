#  Copyright (c) 2020
#  @Author: xiaoweixiang
import bisect
from typing import List


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        res = 0
        for i in staple:
            index = bisect.bisect_right(drinks, x - i)
            res += index
        return res
