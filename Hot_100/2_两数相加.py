"""
    题目描述:
        给你两个 非空 的链表，表示两个非负的整数。
        它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

        请你将两个数相加，并以相同形式返回一个表示和的链表。

        你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    链接: https://leetcode-cn.com/problems/add-two-numbers
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
            链表操作的模拟题；
            使用链表模拟两数相加的过程，注意处理进位信息；
        """
        dumy_head = ListNode()
        
        carry, preNode = 0, dumy_head

        while l1 != None and l2!= None:
            # 正常相加，处理进位
            curNode = ListNode()

            curNode.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10

            preNode.next = curNode
            preNode = curNode

            l1 = l1.next
            l2 = l2.next
        
        # 处理较长的链表
        if l1 != None:
            l = l1
        elif l2 != None:
            l = l2
        else:
            l = None

        while l != None:
            curNode = ListNode()

            curNode.val = (l.val + carry) % 10
            carry = (l.val + carry) // 10

            preNode.next = curNode
            preNode = curNode

            l = l.next
        
        # 处理最高位的进位
        if carry != 0:
            curNode = ListNode(carry)
            preNode.next = curNode
        
        return dumy_head.next

