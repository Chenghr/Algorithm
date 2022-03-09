"""
    题目描述:
        翻转一棵二叉树
    
    链接: https://leetcode-cn.com/problems/invert-binary-tree/
"""

"""
    Tips:
        针对二叉树的问题，解题之前要想清楚到底是用前中后序遍历，还是层序遍历。
"""
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree_levelOrder(self, root: TreeNode) -> TreeNode:

        if root == None:
            return root
        
        queue_ = deque([root])

        while queue_:
            cur = queue_.popleft()

            if cur.left:
                queue_.append(cur.left)
            if cur.right:
                queue_.append(cur.right)
            
            cur.left, cur.right = cur.right, cur.left
        
        return root