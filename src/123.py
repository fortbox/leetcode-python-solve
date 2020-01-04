#  Copyright (c) 2020
#  @Author: xiaoweixiang

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            pre_max = -prices[0]
            for i in range(1, n):
                pre_max = max(pre_max, dp[k - 1][i - 1] - prices[i])
                dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
        return dp[-1][-1]
