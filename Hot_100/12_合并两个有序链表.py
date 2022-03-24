"""
    题目描述:
        将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
    
    链接: https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()

        curNode = dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                curNode.next = list1
                list1 = list1.next
            else:
                curNode.next = list2
                list2 = list2.next
            
            curNode = curNode.next
        
        while list1:
            curNode.next = list1
            list1 = list1.next
            curNode = curNode.next
        
        while list2:
            curNode.next = list2
            list2 = list2.next
            curNode = curNode.next
        
        return dummy_head.next