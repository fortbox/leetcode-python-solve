#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(0, len(arr)):
                if j + i <= len(arr):
                    res += sum(arr[j:i + j])
                    print(arr[j:i + j])
                    # print(res)
        return res


if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    solution = Solution()
    ans = solution.sumOddLengthSubarrays(arr)
    print(ans)
