#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        需要记录list[list]，并且要记录现在在哪一层
        :param logs: 
        :return: 
        """
        current = 0
        step = []
        for log in logs:
            s = log[:-1]
            if s == ".":
                continue
            elif s == "..":
                if current > 0:
                    current -= 1
            else:
                current += 1
        return current


if __name__ == '__main__':
    logs = ["d1/", "d2/", "../", "d21/", "./"]
    solution = Solution()
    ans = solution.minOperations(logs)
    print("ans:", ans)
