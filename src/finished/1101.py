#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        logs.sort(key=lambda ele: ele[0])

        def check(u: UnionFind) -> bool:
            for i in range(1, N):
                if not u.is_connect(i, i - 1):
                    return False
            return True

        uf = UnionFind(N)
        for l in logs:
            uf.merge(l[1], l[2])
            print(uf.parent)
            print("check result: ", check(uf))
            if check(uf):
                return l[0]
        return -1


class UnionFind(object):
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, a: int) -> int:
        if self.parent[a] != a:
            return self.find(self.parent[a])
        return a

    def is_connect(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def merge(self, a: int, b: int) -> None:
        if self.find(a) != self.find(b):
            self.parent[self.find(a)] = self.find(b)


if __name__ == '__main__':
    so = Solution()
    # logs = [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
    #         [20190312, 1, 2], [20190322, 4, 5]]

    logs = [[3, 0, 3], [4, 1, 2], [0, 2, 0], [2, 0, 2], [8, 0, 3], [1, 0, 1], [5, 1, 2], [7, 3, 1], [6, 1, 0],
            [9, 3, 0]]
    N = 4
    # N = 6
    res = so.earliestAcq(logs, N)
    print("res: ", res)
