"""
    题目描述:
        给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

        注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。

    链接: https://leetcode-cn.com/problems/insert-into-a-binary-search-tree
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
            不考虑平衡二叉树的操作，对 BST 的插入一定在叶子节点上
        """
        def _recueseInsert(root, val):
            if root.val > val:
                if root.left == None:
                    root.left = TreeNode(val)
                else:
                    _recueseInsert(root.left, val)
            else:
                if root.right == None:
                    root.right = TreeNode(val)
                else:
                     _recueseInsert(root.right, val)

        if not root:
            return TreeNode(val)
        
        _recueseInsert(root, val)

        return root
        
        
        
        
