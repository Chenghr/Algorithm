"""
    题目描述:
        请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
        实现 LRUCache 类：
            - LRUCache(int capacity):
                以 正整数 作为容量 capacity 初始化 LRU 缓存
            - int get(int key) :
                如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
            - void put(int key, int value) :
                如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。
                如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
            
            函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
    链接: https://leetcode-cn.com/problems/lru-cache 
"""

class ListNode:
    # 双向链表的标头节点
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:
    """
        分析:
            1. 存储结构必须能反应时间序列，否则最久未使用的条件无法满足；-> 链表
            2. 查找以及添加（可能带来的操作）要在O(1)平均时间复杂度内完成； -> 哈希
        
            采用哈希链表；

        双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。
        哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置（node的指针）。

    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0

        # 初始化哈希表
        self.hashMap = dict()

        # 初始化双向链表，头部表示最近使用的节点
        self.LinkHead = ListNode()
        self.LinkTail = ListNode()
        self.LinkHead.next = self.LinkTail
        self.LinkTail.pre = self.LinkHead

    def get(self, key: int) -> int:
        """返回key值指向的元素，并且将其移到链表首部"""
        if key not in self.hashMap:
            return -1

        node = self.hashMap[key]
        
        # node 移动到链表头部
        self._moveToHead(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        """
            1. key 已存在: 更新 val 值
            2. key 不存在:
                1. 元素未满: 直接添加到链表头部
                2. 元素已满: 
                    - 删除链表尾部节点，根据对应 key 值，删除对应哈希表内项；
                    - 从链表头部插入节点
        """
        if key in self.hashMap:
            node = self.hashMap[key]
            node.val = value
            self._moveToHead(node)
        else:
            node = ListNode(key, value)

            if self.count == self.capacity:
                self._removeLinkElement(self.LinkTail.pre)
            
            self._addLinkElement(node)


    def _moveToHead(self, node: ListNode):
        """将双向链表中已有元素移动至头部"""
        # 原位置移除元素
        node.pre.next = node.next
        node.next.pre = node.pre

        # 移动到头部
        self.LinkHead.next.pre = node
        node.next = self.LinkHead.next
        node.pre = self.LinkHead
        self.LinkHead.next = node

    def _removeLinkElement(self, node: ListNode):
        """在双向链表中删除 node, 同步对哈希表以及count进行处理"""
        node.pre.next = node.next
        node.next.pre = node.pre

        self.hashMap.pop(node.key)
        self.count -= 1
    
    def _addLinkElement(self, node: ListNode):
        """在链表头部添加节点; 同步对哈希表以及count进行处理"""
        self.LinkHead.next.pre = node
        node.next = self.LinkHead.next
        node.pre = self.LinkHead
        self.LinkHead.next = node

        self.hashMap[node.key] = node
        self.count += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

a = LRUCache(2)

a.put(2, 1)
a.put(2, 2)
