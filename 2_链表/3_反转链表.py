"""
    题目描述:
        给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
    
    链接: https://leetcode-cn.com/problems/reverse-linked-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
            使用头插法遍历节点即可;
            也可以说是双指针法。
        """
        dummy_head = ListNode()
        curNode = head

        while curNode != None:
            # 暂存下一个节点
            nextNode = curNode.next

            # 插入反转后的链表
            curNode.next = dummy_head.next
            dummy_head.next = curNode

            # 走向下一个节点
            curNode = nextNode
        
        return dummy_head.next