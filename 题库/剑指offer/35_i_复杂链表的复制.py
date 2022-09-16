class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
            先确定 random 链接，再确定 next 链接；
            在每个原先 node 节点后面复制一个节点，
            再次遍历将 random 节点指针确定下来，
            然后将两个链表拆分开即可。
        """
        if not head:
            return None

        curNode = head
        while curNode:  # 复制节点
            copyNode = Node(curNode.val, curNode.next)
            curNode.next = copyNode

            curNode = curNode.next.next
        
        curNode = head
        while curNode:  # 确定 random 索引
            if curNode.random:  # 当前 random 指针是有效索引
                curNode.next.random = curNode.random.next
            curNode = curNode.next.next
        
        pre, curNode, copy_head = head, head.next, head.next
        while curNode.next:  #  确定 next 索引
            pre.next = curNode.next
            curNode.next = curNode.next.next
            
            pre = pre.next
            curNode = curNode.next
        
        return copy_head
        
    def copyRandomList_1(self, head: 'Node') -> 'Node':
        """
            利用哈希表的查询特点，考虑构建 原链表节点 和 新链表对应节点 的键值对映射关系，
            再遍历构建新链表各节点的 next 和 random 引用指向即可。

            算法流程：
                1. 若头节点 head 为空节点，直接返回 nullnull ；
                2. 初始化： 哈希表 dic ， 节点 cur 指向头节点；
                3. 复制链表：
                    建立新节点，并向 dic 添加键值对 (原 cur 节点, 新 cur 节点） ；
                    cur 遍历至原链表下一节点；
                4. 构建新链表的引用指向：
                    构建新节点的 next 和 random 引用指向；
                    cur 遍历至原链表下一节点；
                5. 返回值： 新链表的头节点 dic[cur] ；
        """
        if not head:
            return None
        
        dic = {}

        cur = head
        while cur:  # 复制各节点，建立 原节点 -> 新节点 的映射关系
            
            dic[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:  # 构建新节点的 next 和 random 指向
            dic[cur].next = dic.get(cur.next)  # 使用 get 方法避免 cur.next 为 None
            dic[cur].random = dic.get(cur.random)
        
        return dic[head]

    def copyRandomList_1(self, head: 'Node') -> 'Node':
        """
            利用哈希表存储每个节点对应list 下标；
            两趟遍历:
                第一趟复制节点，利用哈希表存储原始节点对应下标；
                第二趟利用原始节点对应的下标给复制节点的 random 赋值。
        """
        if not head:
            return None

        dic = {}

        node = head
        temp = []

        while node != None:
            dic[node] = len(dic)
            copyNode = Node(node.val)

            if len(temp) > 0:
                temp[-1].next = copyNode
            temp.append(copyNode)
            node = node.next
        
        node, i = head, 0
        while node!= None:
            if node.random in dic:
                random_idx = dic[node.random]
                
                temp[i].random = temp[random_idx]
            
            node = node.next
            i += 1
        
        return temp[0]

   