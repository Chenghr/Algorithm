"""
    题目描述:
        给定二叉搜索树（BST）的根节点和一个值。 
        你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

    链接: https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if root.val == val:
            return root
        
        if root.val < val:
            if root.right:
                return self.searchBST(root.right, val)
            else:
                return None
        
        if root.val > val:
            if root.left:
                return self.searchBST(root.left, val)
            else:
                return None