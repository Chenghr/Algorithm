"""
    题目描述:
        给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

    说明:
        所有节点的值都是唯一的。
        p、q 为不同节点且均存在于给定的二叉搜索树中。
    
    链接: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            相较于普通二叉树的公共祖先问题，BST 树是有序的，那么这个特点应该值得利用。
            在有序树里，从上到下遍历的时候，cur节点是数值在[p, q]区间中则说明该节点cur就是最近公共祖先了。

            因此不同于普通二叉树，我们可以自上向下遍历 -> 前序遍历；
        """
        if not root:
            return None

        if root.val <= max(p.val, q.val) and root.val >= min(p.val, q.val):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left != None and right == None:
            return left
        elif left == None and right != None:
            return right
        else:
            return None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            本题由于从上向下搜索，且一定有解，代码还可以优化一下
        """
        if not root:
            return None

        if root.val > max(p.val, q.val):
            left = self.lowestCommonAncestor(root.left, p, q)
            if left != None:
                return left

        if root.val < min(p.val, q.val):
            right = self.lowestCommonAncestor(root.right, p, q)
            if right != None:
                return right
        
        return root