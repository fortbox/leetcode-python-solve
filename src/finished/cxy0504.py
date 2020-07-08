#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        """
        先找到较大的，然后找到较小的，遍历
        :param num:
        :return:
        """
        res = []
        s = bin(num)[2:]
        print(s)
        i = s.rfind("01")
        j = s.rfind("10")
        print(i)
        print(j)
        a = s[0:i] + "10" + ''.join(sorted(s[i + 2:])) if i >= 0 else "10" + ''.join(sorted(s[i + 2:]))
        b = s[0:j] + "01" + ''.join(sorted(s[j + 2:], reverse=True)) if j >= 0 else "-1"
        print(a)
        print(b)
        return [int(a, 2), int(b, 2)]


if __name__ == '__main__':
    solution = Solution()
    num = 2
    ans = solution.findClosedNumbers(num)
    print("ans:", ans)
