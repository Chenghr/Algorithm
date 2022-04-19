"""

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        """
            1. 逆序链表，输出
            2. 使用栈，逆序
        """
        if not head:
            return []
        
        pre, cur = None, head

        while cur.next:
            node = cur.next

            cur.next = pre
            pre = cur

            cur = node
        
        cur.next = pre

        ans = []

        while cur:
            ans.append(cur.val)
            cur = cur.next
        
        return ans