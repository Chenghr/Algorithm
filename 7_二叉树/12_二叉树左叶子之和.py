"""
    题目描述:
        计算给定二叉树的所有左叶子之和。

    链接: https://leetcode-cn.com/problems/sum-of-left-leaves/
"""


from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
            重点在于左叶子节点的定义:
                左子树不为空，且左子树的左右节点均为空时，则找到一个左子树节点
        """

        if root == None:
            return 0

        summ = 0

        def traversal(node: TreeNode) -> int:
            nonlocal summ

            # 判断是否找到左叶子节点
            if node.left != None and node.left.left == None and node.left.right == None:
                summ += node.left.val
            
            if node.left != None:
                traversal(node.left)
            if node.right != None:
                traversal(node.right)
        
        traversal(root)

        return summ
    
    def sumOfLeftLeaves_v1(self, root: TreeNode) -> int:
        if root == None:
            return 0

        midValue = 0
        
        if root.left != None and root.left.left == None and root.left.right == None:
            midValue += root.left.val
        
        return midValue + self.sumOfLeftLeaves_v1(root.left) + self.sumOfLeftLeaves_v1(root.right)