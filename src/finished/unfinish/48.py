#  Copyright (c) 2020
#  @Author: xiaoweixiang
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        滑动窗口
        :param s: 
        :return: 
        """
        l = list(s)
        res = []
        ans = 0
        for i, val in enumerate(l):
            if val not in res:
                res.append(val)
                if ans < len(res):
                    ans = len(res)
            else:
                j = res.index(val)
                res = res[j + 1:]
                res.append(val)
        return ans


if __name__ == '__main__':
    s = "bbbbb"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)
