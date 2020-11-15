#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
        二维dp
        :param costs:
        :return:
        """
        if not costs: return 0
        dp = [[0 for _ in range(len(costs[0]))] for _ in range(len(costs))]
        dp[0] = costs[0]
        number_of_houses = len(costs)
        number_of_colors = len(costs[0])
        print(number_of_houses)
        print(number_of_colors)
        for i in range(1, number_of_houses):
            for j in range(number_of_colors):
                print("i:", i)
                print("j:", j)
                dp[i][j] = min(dp[i - 1][:j] + dp[i - 1][j + 1:]) + costs[i][j]
        return min(dp[-1])


if __name__ == '__main__':
    solution = Solution()
    costs = [[1, 5, 3], [2, 9, 4]]
    res = solution.minCostII(costs)
    print("res:", res)
