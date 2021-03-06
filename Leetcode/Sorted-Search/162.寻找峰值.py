"""
162.寻找峰值
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设nums[-1] = nums[n] = -∞。

示例 1:
输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。

示例2:
输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5 
解释: 你的函数可以返回索引 1，其峰值元素为 2；
或者返回索引 5， 其峰值元素为 6。

说明:
你的解法应该是O(logN)时间复杂度的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int or None:
        # 线性查找，时间复杂度O(n)
        if not nums:
            return
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1

    def findPeakElement1(self, nums: List[int]) -> int or None:
        # 递归二分查找
        if not nums:
            return

        def search(left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return search(left, mid)
            return search(mid+1, right)
        return search(0, len(nums) - 1)

    def findPeakElement2(self, nums: List[int]) -> int or None:
        # 迭代二分查找
        if not nums:
            return

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
