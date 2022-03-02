"""
    题目描述:
        给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

    链接: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
            删除倒数第 n 个节点，则找到倒数第 n+1 个节点
            双指针，先后指针间隔 n+1 步移动；注意 while 循环的终止条件和间隔计数之间的关系。
            引入虚拟头结点；
        """
        dummyHead = ListNode(0, head)

        count, pre, cur = 0, dummyHead, dummyHead

        while cur.next != None:

            if count >= n:
                pre = pre.next

            cur = cur.next
            count += 1

        # 删除
        pre.next = pre.next.next

        return dummyHead.next
