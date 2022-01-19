"""
    题目描述:
        给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
        假设二叉树中至少有一个节点。

    链接: https://leetcode-cn.com/problems/find-bottom-left-tree-value/
"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
            层次遍历，只保留已知最深层的最左节点
        """
        # 已知 root 不会为 None
        que = deque([(root, 1)])
        leftValue, maxDepth = root.val, 1

        while que:
            node, depth = que.popleft()

            if depth > maxDepth:
                leftValue = node.val
                maxDepth = depth

            if node.left:
                que.append((node.left, depth+1))
            if node.right:
                que.append((node.right, depth+1))

        return leftValue
    
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
            递归解法:
                最后一行: 深度最大的节点;
                最左边的节点: 前序遍历，优先左边搜索
        """
        leftValue, maxDepth = 0, -float('inf')

        def _traverse(root: Optional[TreeNode], curDepth: int) -> int:
            nonlocal leftValue, maxDepth

            # 确定终止条件: 处理叶子节点
            if not root.left and not root.right:
                if curDepth > maxDepth:
                    leftValue = root.val
                    maxDepth = curDepth

            # 确定单层递归的逻辑（递归中包含回溯）
            if root.left:
                curDepth += 1
                _traverse(root.left, curDepth)
                curDepth -= 1
            
            if root.right:
                curDepth += 1
                _traverse(root.right, curDepth)
                curDepth -= 1
        
        _traverse(root, 0)
        return leftValue