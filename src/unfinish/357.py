#  Copyright (c) 2020
#  @Author: xiaoweixiang
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n: return 1
        dp = [0] * (n + 1)
        dp1 = [0] * (n + 1)
        dp[1] = 10
        dp1[1] = 9
        for i in range(2, min(11, n + 1)):
            dp1[i] = dp1[i - 1] * (10 - (i - 1))
            dp[i] = dp1[i] + dp[i - 1]
        if n >= 11: return dp[10]
        return dp[n]
