"""
    题目描述:
        给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
        你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
    
    链接: https://leetcode-cn.com/problems/swap-nodes-in-pairs/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
            使用一个虚拟节点作为头结点，一次向后遍历连个节点；
            注意理清楚节点交换的操作，不要丢失节点即可。
        """
        dummyHead = ListNode()
        dummyHead.next = head
        curNode = dummyHead

        while curNode.next != None and curNode.next.next != None:
            # 交换 curNode.next 与 curNode.next.next

            node2 = curNode.next.next  # 暂存第2个节点，防止丢失

            curNode.next.next = node2.next
            node2.next = curNode.next
            curNode.next = node2

            curNode = curNode.next.next
        
        return dummyHead.next


