#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        """
        滑动窗口，先从2开始，依次变大
        :param array:
        :return:
        """
        res = [-1, -1]
        array1 = array[::1]
        array1.sort()
        for i in range(len(array)):
            if array1[i] != array[i]:
                res[0] = i
                break
        for i in range(len(array) - 1, -1, -1):
            if array1[i] != array[i]:
                res[1] = i
                break
        return res
