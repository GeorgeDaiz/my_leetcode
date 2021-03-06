"""
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def remove_elements(head: ListNode, val: int):
        while head and head.val == val:
            head = head.next

        if not head:
            return
        head_node = head

        while head.next is not None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return head_node
