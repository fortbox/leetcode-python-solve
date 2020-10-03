#  Copyright (c) 2020
#  @Author: xiaoweixiang

class Solution:
    def modifyString(self, s: str) -> str:
        """
        1,记录目前哪些字符未被选中
        2,遍历，然后依次获取
        :param s: 
        :return: 
        """
        l = len(s)
        a = [0] * 26
        for i in range(l):
            if s[i] == '?':
                continue
            n = int(ord(s[i]) - ord('a'))
            print("n: ", n)
            if a[n] == 0:
                a[n] = 1
        aa = []
        for i in range(26):
            if a[i] == 0:
                aa.append(chr(ord('a') + i))

        print("aa:", aa)
        j = 0
        res = []
        for i in range(l):
            if s[i] == '?':
                print("aa[j]", type(aa[j]))
                # s[i] = aa[j][0]
                res.append(aa[j])
                j += 1
                if j == len(aa): j = 0
            else:
                res.append(s[i])
        return ''.join(res)


if __name__ == '__main__':
    s = "????????????????????????????????????????????????????????????????????????????????????????????????????"
    solution = Solution()
    ans = solution.modifyString(s)
    print("ans:", ans)
