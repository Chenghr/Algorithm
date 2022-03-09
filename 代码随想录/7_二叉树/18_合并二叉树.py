"""
    题目描述:
        给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
        你需要将他们合并为一个新的二叉树。
        合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

    注意: 合并必须从两个树的根节点开始。

    链接: https://leetcode-cn.com/problems/merge-two-binary-trees
"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
            同时递归遍历两棵树，合并两棵树
        """
        if root1 == None and root2 == None:
            return None
        
        if root1 != None and root2 == None:
            return root1

        if root1 == None and root2 != None:
            return root2

        if root1 != None and root2 != None:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)

        return root