"""
    题目描述:
        树（Greater Sum Tree），
        使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
        
        提醒一下，二叉搜索树满足下列约束条件:
            节点的左子树仅包含键 小于 节点键的节点。
            节点的右子树仅包含键 大于 节点键的节点。
            左右子树也必须是二叉搜索树。

    链接: https://leetcode-cn.com/problems/convert-bst-to-greater-tree
"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            利用 BST 中序遍历升序的性质，逆中序（右中左）遍历，直接修改值；
        """
        curSum = 0

        def _traverse(root: Optional[TreeNode]):
            if not root:
                return

            _traverse(root.right)

            nonlocal curSum

            root.val += curSum
            curSum = root.val
        
            _traverse(root.left)
        
        _traverse(root)

        return root