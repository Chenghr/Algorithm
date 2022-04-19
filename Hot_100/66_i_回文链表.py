"""
    题目描述:
        给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。
        如果是，返回 true ；否则，返回 false 。
    
    用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
            快慢指针找到链表的中点；
            在找到中点的过程中使用更改前半段链表的指针；记录链表长度（奇偶数的处理方式不同）
            然后分别遍历两段链表来判断回文链表。
        """
        if not head:
            return True
        
        slow_pre, slow, fast = None, head, head

        lenList = 1
        while fast != None and fast.next != None:
            fast = fast.next.next
            
            node = slow.next
            slow.next = slow_pre
            slow_pre = slow
            slow = node
            
            lenList += 2
        
        if not fast:
            lenList -= 1
        
        if lenList % 2 == 0:
            node1 = slow_pre
            node2 = slow
        else:
            node1 = slow_pre
            node2 = slow.next
        
        while node1 and node2:
            if node1.val != node2.val:
                return False

            node1 = node1.next
            node2 = node2.next

        return True

    def isPalindrome(self, head: ListNode) -> bool:
        """
            官方题解；
            整个流程可以分为以下五个步骤：
                找到前半部分链表的尾节点。
                反转后半部分链表。
                判断是否回文。
                恢复链表。
                返回结果。
        """
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start

        # 因为前半部分可能多含有一个节点，因此判断后半部分即可
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
                
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        """链表长为奇数时 slow 指向中点，偶数时指向中间两个数的前者"""
        fast, slow = head, head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        
        return slow

    def reverse_list(self, head):
        """反转链表"""
        previous = None
        current = head

        while current is not None:
            next_node = current.next

            current.next = previous
            previous = current
            current = next_node

        return previous