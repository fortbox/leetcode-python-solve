#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        """
        只想到了暴利和isvisited
        :param points:
        :return:
        """
        d = {}
        x = y = 0
        maxCount = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                k, b = self.f([points[i], points[j]])
                if (k, b) in d.keys():
                    d[(k, b)][0] += 1
                else:
                    d[(k, b)] = [1, (i, j)]
                if d[(k, b)][0] > maxCount or (d[(k, b)][0] == maxCount and
                                               d[(k, b)][1][0] < x) or (d[(k, b)][0] == maxCount and
                                                                        d[(k, b)][1][0] == x and d[(k, b)][1][1] < y):
                    maxCount = d[(k, b)][0]
                    x, y = d[(k, b)][1]
        return [x, y]

    def f(self, points: List[List[int]]) -> List[int]:
        if points[0][0] == points[1][0]:
            return [float('inf'), points[0][0]]
        else:
            return [(points[1][1] - points[0][1]) / (points[1][0] - points[0][0]),
                    (points[0][1] * points[1][0] - points[1][1] * points[0][0]) / (points[1][0] - points[0][0])]
