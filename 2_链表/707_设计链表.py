"""
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。
如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。
                       如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。

https://leetcode-cn.com/problems/design-linked-list/
"""
from typing import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self._length = 0  # 不要忘记更新链表长度

    def get(self, index: int) -> int:
        """获取链表中第 index 个节点的值。如果索引无效，则返回-1。
        """
        # index 从 0 开始，_length 从 1 开始
        if index < -1 or index >= self._length:
            return -1

        curNode = self.dummy_head

        for _ in range(index + 1):
            curNode = curNode.next

        return curNode.val

    def addAtHead(self, val: int) -> None:
        """在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
        """
        newNode = ListNode(val, self.dummy_head.next)
        self.dummy_head.next = newNode

        self._length += 1

    def addAtTail(self, val: int) -> None:
        """将值为 val 的节点追加到链表的最后一个元素。
        """
        # 先找到最后一个链表节点
        curNode = self.dummy_head
        
        # _length表示实际长度
        for _ in range(self._length):
            curNode = curNode.next
        
        curNode.next = ListNode(val)

        self._length += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """在链表中的第 index 个节点之前添加值为 val  的节点。
           如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
        """
        if index < 0:
            # 如果index小于0，则在头部插入节点
            self.addAtHead(val)

        elif index == self._length:
            # 如果 index 等于链表的长度，则该节点将附加到链表的末尾
            self.addAtTail(val)

        elif index <= self._length -1:
            # 在第 index 个节点前添加节点，注意 _length 的计数值起始为1，index的起始值为0
            curNode = self.dummy_head

            # 找到第 index-1 个节点
            for _ in range(index):
                curNode = curNode.next
            
            newNode = ListNode(val, curNode.next)
            curNode.next = newNode
            
            self._length += 1
        else:
            # index 大于链表长度，则不会插入节点
            pass

    def deleteAtIndex(self, index: int) -> None:
        """如果索引 index 有效，则删除链表中的第 index 个节点。
        """
        # index 索引不可超过链表长度
        if 0 <= index < self._length:
            curNode = self.dummy_head

            # 找到第 index-1 个节点
            for _ in range(index):
                curNode = curNode.next
            
            curNode.next = curNode.next.next

            self._length -= 1