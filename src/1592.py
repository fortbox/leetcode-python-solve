#  Copyright (c) 2020
#  @Author: xiaoweixiang
class Solution:
    def reorderSpaces(self, text: str) -> str:
        tt = text.split(" ")
        t = []
        for i in tt:
            if i != '':
                t.append(i)

        print(t)
        count = 0
        for n in text:
            if n == ' ':
                count += 1
        print("count: ", count)
        l = len(t)
        print("l:", l)
        num, d = 0, 0
        if l > 1:
            num = count // (l - 1)
            d = count % (l - 1)
        else:
            d = count
        print("num:", num)
        print("d:", d)
        s = ""
        for i in range(num):
            s += " "
        ss = ""
        for i in range(d):
            ss += " "

        res = ""
        for i in t:
            res += i + s
        res = res[:len(res) - num]
        res += ss
        return res


if __name__ == '__main__':
    text = "  this   is  a sentence "
    solution = Solution()
    ans = solution.reorderSpaces(text)
    print("ans: ", ans)
