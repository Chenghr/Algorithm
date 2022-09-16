"""
    题目描述:
        给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
        叶子节点 是指没有子节点的节点。

    链接: https://leetcode-cn.com/problems/binary-tree-paths/
"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
            遍历所有的节点 -> 深度遍历，先根遍历;
            存储路径，path
        """
        result = []

        def traversal_preOrder(node: Optional[TreeNode], path: str):
            
            nonlocal result

            if node.left == None and node.right == None:
                path += str(node.val)
                result.append(path)
            
            # 中
            path = path + str(node.val) + '->'
            
            # 左
            if node.left != None:
                traversal_preOrder(node.left, path)
            
            # 右
            if node.right != None:
                traversal_preOrder(node.right, path)
            
        traversal_preOrder(root, '')

        return result

