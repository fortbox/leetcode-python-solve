#  Copyright (c) 2020
#  @Author: xiaoweixiang
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 1, 2
        for i in range(4, n + 1):
            tmp = 0
            for j in range(1, i):
                dp[i] = max(dp[i], max(dp[j], j) * max(i - j, dp[i - j]))
        return dp[n]


if __name__ == '__main__':
    n = 10
    solution = Solution()
    ans = solution.integerBreak(n)
    print(ans)
