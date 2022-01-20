"""
    题目描述:
        给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
        差值是一个正数，其数值等于两值之差的绝对值。
    
    题目链接: https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        """
            思路:
                BST 树进行中序遍历，得到的值都是从小到大分布的；
                最小差值一定是在相邻两个数之间的差值。
            
            具体:
                中序遍历；
        """
        nums = []

        def _inorder_traverse(root: TreeNode):
            if not root:
                return 
            
            _inorder_traverse(root.left)

            nonlocal nums
            nums.append(root.val)

            _inorder_traverse(root.right)

        _inorder_traverse(root)
        
        minVal = float('inf')
        
        for i in range(1, len(nums)):
            minVal = min(minVal, nums[i]-nums[i-1])
        
        return minVal
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        """
            优化: 
                递归中记录前一个节点的指针，降低空间复杂度
        """

        minDis, preNode = float('inf'), None

        def _traverse(root: TreeNode) -> None:

            if not root:
                return 

            _traverse(root.left)

            nonlocal minDis, preNode

            if preNode is None:
                preNode = root
            else:
                curDis = root.val - preNode.val
                minDis = min(minDis, curDis)
                preNode = root
            
            _traverse(root.right)
        
        _traverse(root)

        return minDis