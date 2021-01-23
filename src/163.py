from typing import List


class Solution:
    def merge(self, a: int, b: int, l: List) -> List[str]:
        if a == b:
            l.append(str(a))
        elif a < b:
            l.append(str(a) + "->" + str(b))
        return l

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        if len(nums) == 0:
            start, end = lower, upper
            res = self.merge(start, end, res)
            return res
        if len(nums) == 1:
            start = lower
            end = nums[0] - 1
            res = self.merge(start, end, res)
            start = nums[0] + 1
            end = upper
            res = self.merge(start, end, res)
            return res
        for i in range(len(nums)):
            if i == 0:
                start, end = lower, nums[i]
                res = self.merge(start, end, res)
            if i < len(nums) - 1:
                start, end = nums[i] + 1, nums[i + 1] - 1
                res = self.merge(start, end, res)
            if i == len(nums) - 1:
                start, end = nums[i] + 1, upper
                res = self.merge(start, end, res)

        return res


if __name__ == '__main__':
    nums = [1000000000]
    lower = 0
    upper = 1000000000
    so = Solution()
    ans = so.findMissingRanges(nums, lower, upper)
    print("ans:", ans)
