# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList_1(self, head: ListNode) -> ListNode:
        """迭代法"""
        if not head:
            return head
        
        pre, cur = None, head

        while cur:
            node = cur.next

            cur.next = pre
            pre = cur

            cur = node
        
        return pre
    
    def reverseList(self, head: ListNode) -> ListNode:
        """递归法"""
        # 边界
        if not head or not head.next:
            return head
        
        # 单层递归逻辑
        newHead = self.reverseList(head.next)
        head.next.next = head  # 保证下一个节点的反向指向自己
        head.next = None  # 最开始的节点的后续节点要是空值

        return newHead