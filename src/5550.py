#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        tmp = [0] * length
        for i in range(length): tmp[i] = code[i]
        if k == 0: return [0] * length
        if k > 0:
            for i in range(length):
                if i + k < length:
                    code[i] = sum(tmp[i + 1:i + k + 1])
                else:
                    code[i] = sum(tmp[i + 1:] + tmp[0:k - (length - i - 1)])
        else:
            k = -k
            for i in range(length):
                if i >= k:
                    code[i] = sum(tmp[i - k:i])
                else:
                    code[i] = sum(tmp[0:i] + tmp[length - k + i:])
        return code


if __name__ == '__main__':
    code = [5, 7, 1, 4]
    k = 3
    so = Solution()
    ans = so.decrypt(code, k)
    print(ans)
