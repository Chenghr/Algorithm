"""输入两个链表，找出它们的第一个公共节点。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
            新的解法: 走过相同的距离，就能遇见你
                设交集链表长 c ,链表 1 除交集的长度为 a，链表 2 除交集的长度为 b，有
                    a + c + b = b + c + a
        """
        node1, node2 = headA, headB
        
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """经典题目
        """
        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB

        while nodeA:
            nodeA = nodeA.next
            lenA += 1
        
        while nodeB:
            nodeB = nodeB.next
            lenB += 1
        
        if lenA < lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        
        # 长的先走
        nodeA = headA
        for _ in range(lenA - lenB):
            nodeA = nodeA.next
        
        nodeB = headB
        while nodeA:
            if nodeA == nodeB:
                return nodeA
            
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        return None