class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """递归--官解写法
        """
        # 边界处理
        if not l1:
            return l2
        if not l2:
            return l1
        
        # 单层逻辑
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1.next, l2)
            return l2

        
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """递归
        """
        if l1 == None and l2 == None:
            return None
        
        if l1 != None and l2 == None:
            return l1
        
        if l1 == None and l2 != None:
            return l2
        
        # 单层逻辑
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1.next, l2)
            return l2

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """迭代
        """
        dummy_head = ListNode()

        head1, head2, cur = l1, l2, dummy_head
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                cur = cur.next
                head1 = head1.next
            else:
                cur.next = head2
                cur = cur.next
                head2 = head2.next

        if head1:  # 注意这里不用再 while 遍历
            cur.next = head1
        else:
            cur.next = head2
        
        return dummy_head.next