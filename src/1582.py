#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        遍历每个点，如果是则遍历
        :param mat:
        :return:
        """
        count = 0
        row = len(mat)
        col = len(mat[0])
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    flag = False
                    for k in range(col):
                        if k != j and mat[i][k] == 1:
                            flag = True
                            break
                    if flag:
                        continue
                    for k in range(row):
                        if k != i and mat[k][j] == 1:
                            flag = True
                            break
                    if flag:
                        continue
                    count += 1
        return count


if __name__ == '__main__':
    mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
    solution = Solution()
    ans = solution.numSpecial(mat)
    print(ans)
