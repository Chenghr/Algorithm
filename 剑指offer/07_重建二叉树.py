class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """前中序实现二叉树"""
        if len(preorder) == 0:
            return None 

        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        leftLength = inorder.index(preorder[0])
        # 越界切片会返回空list
        left = self.buildTree(preorder[1: leftLength+1], inorder[: leftLength])
        right = self.buildTree(preorder[leftLength+1:], inorder[leftLength+1:])

        return TreeNode(preorder[0], left, right)