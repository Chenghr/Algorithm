"""输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        fast, count = head, 0
        while count != k and fast:
            # fast 先指向第 k+1 个节点， slow 指向第 1 个，中间刚好间隔 k 个节点
            fast = fast.next
            count += 1

        if count != k:
            return None

        slow = head
        while fast:
            fast = fast.next
            slow = slow.next
        
        return slow
