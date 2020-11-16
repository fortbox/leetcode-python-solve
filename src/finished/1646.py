#  Copyright (c) 2020
#  @Author: xiaoweixiang

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        """
        定义一个数组，然后遍历一遍
        :param n: 
        :return: 
        """
        ans = 1
        if n < 1: return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[int(i / 2)]
            else:
                nums[i] = nums[int(i // 2)] + nums[int(i // 2) + 1]
            ans = max(ans, nums[i])
        return ans


if __name__ == '__main__':
    so = Solution()
    res = so.getMaximumGenerated(7)
    print(res)
