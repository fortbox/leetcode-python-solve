#  Copyright (c) 2020
#  @Author: xiaoweixiang
class Solution:
    def maxPower(self, s: str) -> int:
        n = 1
        ans = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                n += 1
                if n > ans:
                    ans = n
            else:
                if n > ans:
                    ans = n
                n = 1
        return ans
