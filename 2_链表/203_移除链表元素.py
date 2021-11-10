"""
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
https://leetcode-cn.com/problems/remove-linked-list-elements/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(val=-1, next=head)

        curNode = dummy_head

        while curNode.next != None:
            if curNode.next.val == val:
                # 删除下个节点
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        
        return dummy_head.next