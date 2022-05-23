"""
    给定一个整数数组，它表示BST(即 二叉搜索树 )的 先序遍历 ，构造树并返回其根。
    保证 对于给定的测试用例，总是有可能找到具有给定需求的二叉搜索树。

    https://leetcode.cn/problems/construct-binary-search-tree-from-preorder-traversal/
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
            根据 BST 的性质，可以精确地判断出左子树区间和右子树区间；
            左子树区间的元素均小于当前值，右子树的区间均大于当前值。

            这里可以重新创建一个辅助函数，避免重复赋值数组。
        """
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])

        if len(preorder) == 1:              # 提前终止搜索
            return root

        left, right = 1, len(preorder)  # 找第一个大于 root.val 的元素下标
        while left < right:
            mid = (left + right) // 2
            if preorder[mid] > root.val:
                right = mid
            else:
                left = mid + 1
        
        root.left = self.bstFromPreorder(preorder[1: left])
        root.right = self.bstFromPreorder(preorder[left:])

        return root
