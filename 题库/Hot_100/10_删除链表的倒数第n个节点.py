"""
    题目描述:
        给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
    
    链接: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
            删除倒数第 n 个节点，要找到倒数第 n+1 个节点；
            注意对头结点的删除，因此要引入虚拟头结点。
        """
        dummy_head = ListNode()
        dummy_head.next = head

        preNode, curNode, count = dummy_head, dummy_head, 0

        while curNode != None:

            curNode = curNode.next

            if count == n+1:
                # 引入了虚拟头结点，因此 count 计数至 n+1
                preNode = preNode.next
            else:
                count += 1
        
        preNode.next = preNode.next.next

        return dummy_head.next

        """
            其他思路求解:
                1. 计算链表长度
                2. 使用栈，利用栈先进后出的原则，
                   弹出栈的第 n 个节点就是需要删除的节点，并且目前栈顶的节点就是待删除节点的前驱节点
        """