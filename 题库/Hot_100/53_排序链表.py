"""
    题目描述:
        给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

    进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
    链接: https://leetcode-cn.com/problems/sort-list/
"""

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            自顶向下归并排序
            
            对链表自顶向下归并排序的过程如下。
                - 找到链表的中点，以中点为分界，将链表拆分成两个子链表。寻找链表的中点可以使用快慢指针的做法。
                - 对两个子链表分别排序。
                - 将两个排序后的子链表合并，得到完整的排序后的链表。
        """
        def merge(head1: ListNode, head2: ListNode):
            """合并两个有序链表"""
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2

            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next

            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2

            return dummyHead.next

        def sortPart(head: ListNode, tail: ListNode):
            """归并排序，链表递减，左闭右开
            """
            if not head:
                return head
            
            if head.next == tail:
                # 左闭右开，分成两个链表
                head.next = None
                return head

            slow, fast = head, head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            # slow 指向链表中点

            return merge(sortPart(head, slow), sortPart(slow, tail))

        return sortPart(head, None)