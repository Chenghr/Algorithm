"""
    给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
    返回删除后的链表的头节点。

    保证链表中节点的值互不相同
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        """不使用虚拟头结点
        """
        if not head:
            return None
        
        if head.val == val:
            return head.next
        
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        
        if cur:
            pre.next = cur.next
        
        return head


    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        """使用虚拟头结点
        """
        if not head:
            return None
        
        dummy_head = ListNode()
        dummy_head.next = head
        curNode = dummy_head

        while curNode.next:
            if curNode.next.val == val:
                curNode.next = curNode.next.next
                break
        
        return dummy_head.next