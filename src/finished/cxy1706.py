#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        """
        参考其他人
        :param n:
        :return:
        """
        s = str(n)
        x = 2
        count = 0
        for i in range(len(s)):
            current = int(s[i])
            high = 0 if s[:i] == '' else int(s[:i])
            low = 0 if s[i + 1:] == '' else int(s[i + 1:])
            if current > x:
                count += (high + 1) * (10 ** len(s[i + 1:]))
            elif current < x:
                count += high * (10 ** len(s[i + 1:]))
            else:
                count += high * (10 ** len(s[i + 1:])) + low + 1
        return count

    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        n1, n2 = float("-inf"), float("inf")
        res = len(words)
        for index, s in enumerate(words):
            if s == word1:
                n1 = index
            elif s == word2:
                n2 = index
            res = min(res, abs(n1 - n2))
        return res
