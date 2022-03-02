"""
    题目描述:
        给你两个单链表的头节点 headA 和 headB ，
        请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
    
    链接: https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
            如果链表相交，那么从交点到终点的节点应该相同；
            因此先分别遍历两个链表，得到链表长度，然后让较长的链表先走相差的节点，再比较节点。
        """
        lenA, lenB = 0, 0

        curNode = headA
        while curNode != None:
            curNode = curNode.next
            lenA += 1
        
        curNode = headB
        while curNode != None:
            curNode = curNode.next
            lenB += 1
        
        if lenA < lenB:
            # 保证 A 是较长的那个链表
            lenA, lenB = lenB, lenA
            headA, headB = headB, headA
        
        curA, curB = headA, headB

        for _ in range(lenA-lenB):
            curA = curA.next
        
        while curA != None and curB != None:
            if curA == curB:
                return curA
            
            curA = curA.next
            curB = curB.next
        
        return None