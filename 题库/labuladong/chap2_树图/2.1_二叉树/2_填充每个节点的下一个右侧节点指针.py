"""
    给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点
    填充它的每个 next 指针，让这个指针指向其下一个右侧节点。
    如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

    初始状态下，所有 next 指针都被设置为 NULL。
"""

from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """遍历的解决思路；本题好像不能用分解问题的思路来做
        """
        def traverse(root: Node):
            """先根遍历；
            """
            if not root:
                return
            
            if root.left:  # 非叶节点
                root.left.next = root.right

                if root.next:  # 子节点的跨域相连
                    root.right.next = root.next.left
            
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        return root
    
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """另一种写法
        """
        def traverse(node1: Node, node2: Node):
            if not node1 or not node2:
                return
            
            node1.next = node2                  # 传入的两个节点串起来
            
            traverse(node1.left, node1.right)   # 连接相同父节点的两个子节点
            traverse(node2.left, node2.right)
            traverse(node1.right, node2.left)   # 连接跨越父节点的两个子节点
        
        if not root:
            return None
        
        traverse(root.left, root.right)
        return root
        