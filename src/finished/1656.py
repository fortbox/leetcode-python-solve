#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 1
        self.l = [0 for _ in range(n + 1)]

    def insert(self, id: int, value: str) -> List[str]:
        self.l[id] = value
        res = []
        l_id = []
        if self.ptr == id:
            for i in range(id, len(self.l)):
                if self.l[i] != 0:
                    res.append(self.l[i])
                    l_id.append(i)
                else:
                    break
        if len(res) != 0: self.ptr = l_id[-1] + 1
        return res
