"""
    题目描述:
        给定一个不含重复元素的整数数组 nums 。

        一个以此数组直接递归构建的 最大二叉树 定义如下:
            二叉树的根是数组 nums 中的最大元素。
            左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
            右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。

        返回有给定数组 nums 构建的 最大二叉树 。

    链接: https://leetcode-cn.com/problems/maximum-binary-tree
"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
            递归构建二叉树，以最大数为根节点，类似15中的构造思路即可
        """
        if len(nums) == 0:
            return None
        
        root = TreeNode(max(nums))

        # 叶节点
        if len(nums) == 1:
            return root
        
        # 中间节点
        splitIdx = nums.index(max(nums))

        root.left = self.constructMaximumBinaryTree(nums[:splitIdx])
        root.right = self.constructMaximumBinaryTree(nums[splitIdx+1:])

        return root