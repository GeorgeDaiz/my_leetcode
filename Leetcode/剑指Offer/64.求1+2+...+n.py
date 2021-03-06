"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：
输入: n = 3
输出:6

示例 2：
输入: n = 9
输出:45

限制：
1 <= n<= 10000
"""


class Solution:
    # 逻辑运算符短路效应
    def sumNums(self, n: int) -> int:
        def __init__(self):
            self.res = 0

        def sumNums(self, n: int) -> int:
            n > 1 and self.sumNums(n - 1)
            self.res += n
            return self.res


class Solution1:
    # 快速乘
    def helper(self, A, B):
        ans = B and self.helper(A << 1, B >> 1)
        ans += B & 1 and A
        return ans

    def sumNums(self, n: int) -> int:
        return self.helper(n, n + 1) >> 1
