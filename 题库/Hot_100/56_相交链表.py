"""
    题目描述:
        给你两个单链表的头节点 headA 和 headB;
        请你找出并返回两个单链表相交的起始节点。
        如果两个链表不存在相交节点，返回 null 。
    
    进阶：你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？

    题目描述: https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        
        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB

        while nodeA != None:
            nodeA = nodeA.next
            lenA += 1
        
        while nodeB != None:
            nodeB = nodeB.next
            lenB += 1
        
        if lenA < lenB:
            # 保证 A 是较长的那个
            lenA, lenB = lenB, lenA
            headA, headB = headB, headA
        
        diff = lenA - lenB
        nodeA, nodeB = headA, headB

        while diff > 0:
            nodeA = nodeA.next
            diff -= 1
        
        while nodeA != None:
            if nodeA == nodeB:
                return nodeA
            
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        return None