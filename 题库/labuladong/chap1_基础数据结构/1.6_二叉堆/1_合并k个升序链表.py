"""
    题目描述:
        给你一个链表数组，每个链表都已经按升序排列。
        请你将所有链表合并到一个升序链表中，返回合并后的链表。

    链接: https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""

from typing import List, Optional
from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
            使用优先队列降低在 k 个节点中寻找最小值的时间开销；
            注意要重载运算符，使得元素满足比较的要求。
        """
        def __lt__(a: ListNode, b:ListNode):
            return a.val < b.val
        
        ListNode.__lt__ = __lt__

        pq = PriorityQueue()

        for node in lists:
            if node:
                pq.put(node)
        
        dummyHead = ListNode()
        curNode = dummyHead

        while pq.qsize() != 0:
            node = pq.get()

            if node.next:
                pq.put((node.next.val, node.next))

            curNode.next = node
            curNode = node
        
        return dummyHead.next

