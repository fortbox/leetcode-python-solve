#  Copyright (c) 2020
#  @Author: xiaoweixiang
import bisect
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        先排序，然后比较每一位与在数组中的位置作比较，如果数字==len-位置，则+1
        :param nums: 
        :return: 
        """
        nums.sort()
        size = len(nums)
        for i in range(size):
            for j in range(nums[-1]):
                index = bisect.bisect_left(nums, j)
                if j == size - index:
                    return j
        return -1


if __name__ == '__main__':
    nums = [0, 4, 3, 0, 4]
    solution = Solution()
    ans = solution.specialArray(nums)
    print("ans:", ans)
