"""
给定一个包含 0, 1, 2, ..., n中n个数的序列，找出 0 .. n中没有出现在序列中的那个数。

示例 1:
输入: [3,0,1]
输出: 2

示例2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8

说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
"""


class Solution:
    def missingNumber(self, nums: list) -> int:
        return (len(nums) + 1) * len(nums) // 2 - sum(nums)
