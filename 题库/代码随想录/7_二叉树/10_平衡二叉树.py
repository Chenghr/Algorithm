"""
    题目描述:
        给定一个二叉树，判断它是否是高度平衡的二叉树。
        本题中，一棵高度平衡二叉树定义为:
            一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
    
    链接: https://leetcode-cn.com/problems/balanced-binary-tree/
"""

from typing import List, Optional
from collections import deque

import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced_recurse(self, root: TreeNode) -> bool:
        """
            分析:
                1. 求树的高度 -> 后序遍历
                2. 递归的解决思路:

                 - 参数: 当前传入节点。
                   返回值: 以当前传入节点为根节点的树的高度。

                 - 终止条件:
                    遇到空节点了为终止，返回0，表示当前节点为根节点的树高度为0
                
                 - 单层递归的逻辑:
                    分别求出其左右子树的高度，然后如果差值小于等于1，则返回当前二叉树的高度，
                    否则则返回-1，表示已经不是二叉平衡树了。
        """
        def getHeight(node: Optional[TreeNode]) -> int:
            """返回值为 -1 表示已经不是平衡二叉树了；
                否则返回值是以该节点为根节点树的高度
            """
            if node == None:
                return 0

            # 左
            leftHeight = getHeight(node.left)
            if leftHeight == -1:
                return -1
            
            # 右
            rightHeight = getHeight(node.right)
            if rightHeight == -1:
                return -1
            
            # 中
            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            return 1 + max(leftHeight, rightHeight)
        
        rootHeight = getHeight(root)

        if rootHeight == -1:
            return False
        
        return True
    
    def isBalanced_afterOrder(self, root: TreeNode) -> bool:
        """
            本题的迭代方式可以先定义一个函数，专门用来求高度。
            这个函数通过栈模拟的后序遍历找每一个节点的高度
            （其实是通过求传入节点为根节点的最大深度来求的高度）

            本题迭代法的效率并不高，做了很多重复计算，不提倡使用，但是可以了解流程
        """

        def getDepth(root: Optional[TreeNode]):
            
            if root == None:
                return 0

            stack = [root]

            depth, result = 0, 0

            while stack:
                node = stack.pop()

                if node:
                    # 中
                    stack.append(node)
                    stack.append(None)  # 添加标记

                    depth += 1

                    # 右、左
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
                else:
                    node = stack.pop()
                    depth -= 1
                
                result = max(result, depth)
            
            return depth

        if root == None:
            return True
        
        stack = [root]

        while stack:
            node = stack.pop()

            leftDepth = getDepth(node.left)
            rightDepth = getDepth(node.right)

            if abs(leftDepth - rightDepth) > 1:
                return False
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        return True