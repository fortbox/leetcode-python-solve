#  Copyright (c) 2020
#  @Author: xiaoweixiang


class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        uf = Unionfind()
        for i in range(len(A)):
            uf.merge(ord(A[i]) - ord('a'), ord(B[i]) - ord('a'))
        print(uf.parent)
        res = []
        for cc in S:
            print("cc: ", cc)
            dd = ord(cc) - ord('a')
            ee = uf.find(dd)
            for i in range(26):
                if uf.find(i) == ee:
                    ff = chr(i + ord('a'))
                    if cc > ff:
                        cc = ff
            print("lol: ", cc)
            res.append(cc)
        return "".join(res)


class Unionfind:
    """
    find
    isConnect
    merge
    """

    def __init__(self):
        self.parent = [int(i) for i in range(26)]

    def find(self, a: int) -> int:
        if self.parent[a] != a:
            return self.find(self.parent[a])
        return a

    def is_connect(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def merge(self, a: int, b: int) -> None:
        a_father = self.find(a)
        b_father = self.find(b)
        if a_father == b_father:
            return
        self.parent[a_father] = b_father


if __name__ == '__main__':
    A = "parker"
    B = "morris"
    S = "parser"
    solution = Solution()
    k = solution.smallestEquivalentString(A, B, S)
    print("k: ", k)
