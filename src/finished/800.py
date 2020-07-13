#  Copyright (c) 2020
#  @Author: xiaoweixiang
class Solution:

    def similarRGB(self, color: str) -> str:
        """
        看了答案才明白题目意思
        :param color:
        :return:
        """

        def similarity(hex1, hex2) -> int:
            r1, g1, b1 = hex1 >> 16, (hex1 >> 8) % 256, hex1 % 256
            r2, g2, b2 = hex2 >> 16, (hex1 >> 8) % 256, hex1 % 256
            return -(r1 - r2) ** 2 - (g1 - g2) ** 2 - (b1 - b2) ** 2

        hex1 = int(color[1:], 16)
        ans = 0
        for r in range(16):
            for g in range(16):
                for b in range(16):
                    hex2 = 17 * r * (1 << 16) + 17 * g * (1 << 8) + 17 * b
                    if similarity(hex1, hex2) > similarity(hex1, ans):
                        ans = hex2
        return '#{:06x}'.format(ans)
