#  Copyright (c) 2020
#  @Author: xiaoweixiang
import typing


class Solution:
    def busyStudent(self, startTime: typing.List[int], endTime: typing.List[int], queryTime: int) -> int:
        ans = 0
        for i in range(len(startTime)):
            s = startTime[i]
            e = endTime[i]
            if e >= queryTime >= s:
                ans += 1
        return ans
