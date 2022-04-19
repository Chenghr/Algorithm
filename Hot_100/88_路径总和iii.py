"""
    题目描述:
        给定一个二叉树的根节点 root ，和一个整数 targetSum ，
        求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

        路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

    链接: https://leetcode-cn.com/problems/path-sum-iii
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """使用先根遍历，记录路径值"""
        path = []
        count = 0
        def preTraverse(root: TreeNode):
            nonlocal path, count

            if node