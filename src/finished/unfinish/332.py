#  Copyright (c) 2020
#  @Author: xiaoweixiang
from queue import Queue
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # bfs dfs都可，我感觉bfs更简单
        q = Queue()
        q.put("JFK")
        ans = []
        is_visited = []
        while q.qsize() > 0:
            g = q.get()
            ans.append(g)
            l = []
            for i in range(len(tickets)):
                if tickets[i][0] == g and i not in is_visited:
                    is_visited.append(i)
                    l.append((tickets[i][1], i))
            l.sort()
            print(l)
            if len(l) > 0:
                q.put(l[0][0])
                is_visited.append(l[0][1])
        return ans


if __name__ == '__main__':
    solution = Solution()
    t = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    res = solution.findItinerary(t)
    print(res)
