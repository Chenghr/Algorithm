"""
    给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:

        创建一个根节点，其值为 nums 中的最大值。
        递归地在最大值 左边 的 子数组前缀上 构建左子树。
        递归地在最大值 右边 的 子数组后缀上 构建右子树。
        返回 nums 构建的 最大二叉树 。
"""

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
            分解的思路;
            构造树 = 根节点 + 左子树节点 + 右子树节点
        """ 
        if len(nums) == 0:  # 终点
            return None
        
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:nums.index(max(nums))])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(max(nums))+1: ])

        return root