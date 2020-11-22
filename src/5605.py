#  Copyright (c) 2020 
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = "".join(word1)
        s2 = "".join(word2)
        return "".join(word1) == "".join(word2)


if __name__ == '__main__':
    solution = Solution()
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    ans = solution.arrayStringsAreEqual(word1, word2)
    print(ans)
