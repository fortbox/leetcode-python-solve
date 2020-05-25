#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        深度优先，遍历每个点，对每个点来判断
        如果为O的可以到达边界，则这个点不处理，否则处理
        对于每个点遍历的时候都要有一个数组来记录哪些被访问过
        先定义一个上、下、左、右
        :param board:
        :return:
        """
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(board, row, col):
            board[row][col] = '#'
            for i, j in moves:
                newx, newy = row + i, col + j
                if 0 <= newx < m and 0 <= newy < n and board[newx][newy] == 'O':
                    dfs(board, newx, newy)

        if not board:
            return []
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == 'O':
                    dfs(board, i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
