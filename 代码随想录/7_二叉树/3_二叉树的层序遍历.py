"""
    题目描述:
        给你二叉树的根节点 root ，返回其节点值的层序遍历，即逐层地，从左到右访问所有节点。

    链接:https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
"""

from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder_recur(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        result = []

        def traversal(root, depth):
            nonlocal result

            if len(result) > depth:
                result[depth].append(root.val)
            else:
                result.append([root.val])
            
            if root.left is not None:
                traversal(root.left, depth+1)
            if root.right is not None:
                traversal(root.right, depth+1)
        
        traversal(root, 0)

        return result   
        
    def levelOrder_queue(self, root: TreeNode) -> List[List[int]]:
        """注意题目要求每层元素为一个 list, 因此要记录层数
        """
        if root is None:
            return []

        result = []
        # 创建 dueue 队列
        # 初始传入的为可迭代序列, 此处是 list; 另外要记录层数，因此 list 内应该是一个 tuple.
        nodeQue = deque([(root, 0)])

        while (len(nodeQue) != 0):
            node, depth = nodeQue.popleft()

            if len(result) > depth:
                # 存储到对应层去
                result[depth].append(node.val)
            else:
                # 第一次存储当前层的元素
                result.append([node.val])
                

            if node.left is not None:
                nodeQue.append((node.left, depth+1))
            if node.right is not None:
                nodeQue.append((node.right, depth+1))
            
        return result