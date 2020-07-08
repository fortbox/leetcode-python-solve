#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        """
        完全没思路啊
        :param dictionary:
        :param sentence:
        :return:
        """
        dp = [0] * (len(sentence) + 1)
        for i in range(1, len(sentence) + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i - 1, -1, -1):
                s = sentence[j:i]
                if s in dictionary:
                    dp[i] = min(dp[i], dp[j])
        return dp[-1]


so = Solution()
dictionary = ["looked", "just", "like", "her", "brother"]
sentence = "jesslookedjustliketimherbrother"
ans = so.respace(dictionary, sentence)
print(ans)
