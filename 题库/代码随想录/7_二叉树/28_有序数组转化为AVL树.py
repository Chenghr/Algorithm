"""
    题目描述:
        给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
        高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

    链接: https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
            每次选取有序数组的中间数值作为节点进行插入，即可获得 AVL 树
        """
        if len(nums) == 0:
            return None
            
        if len(nums) == 1:
            return TreeNode(nums[0])

        val = nums[int(len(nums)/2)]

        root = TreeNode(val)
        root.left = self.sortedArrayToBST(nums[: int(len(nums)/2)])
        root.right = self.sortedArrayToBST(nums[int(len(nums)/2)+1 : ])
        
        return root
        
