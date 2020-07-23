#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        """
        一点思路都没有呢
        应该是正则匹配
        看了解题，卧槽，被实例误导了
        :param queries:
        :param pattern:
        :return:
        """
        p = tuple(c for c in pattern if c.isupper())

        def f(words: str) -> bool:
            i = 0
            for c in pattern:
                j = words.find(c, i)
                if j == -1:
                    return False
                i = j + 1
            return p == tuple(c for c in words if c.isupper())

        return map(f, queries)
