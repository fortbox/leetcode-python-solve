#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        dp[0] = 0
        for i in range(1, num + 1):
            if i % 2 == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i // 2]
        return dp
