#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        tmp = []
        for i in range(len(intervals)):
            if i == 0:
                tmp.append(intervals[i])
            else:
                if tmp[-1][1] >= intervals[i][0]:
                    tmp[-1][0] = min(tmp[-1][0], intervals[i][0])
                    tmp[-1][1] = max(tmp[-1][1], intervals[i][1])
                else:
                    tmp.append(intervals[i])

        return tmp


if __name__ == '__main__':
    solution = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    ans = solution.merge(intervals)
    print(ans)
