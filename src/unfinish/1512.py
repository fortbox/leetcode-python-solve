#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    ans += 1
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    solution = Solution()
    result = solution.numIdenticalPairs(nums)
    print("result=", result)
