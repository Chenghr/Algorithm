"""
    递归函数何时要有返回值

    题目1描述:
        给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
        判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
        叶子节点 是指没有子节点的节点。

    链接: https://leetcode-cn.com/problems/path-sum

    题目2描述:
        给你二叉树的根节点 root 和一个整数目标和 targetSum ，
        找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
        叶子节点 是指没有子节点的节点。

    链接: https://leetcode-cn.com/problems/path-sum-ii
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
            先序遍历，判断是否存在一个路径；
            递归过程找一个正确解，递归完成都没找到一个正确解，则返回False
        """
        
        def _traversal(root: TreeNode, targetSum: int):

            # 判断是否为叶子节点
            if root.left == None and root.right == None:
                if root.val == targetSum:
                    return True
                else:
                    return False
            
            # 中间节点且可以向下寻找
            if root.left:
                if _traversal(root.left, targetSum-root.val):
                    return True
            if root.right:
                if _traversal(root.right, targetSum-root.val):
                    return True
            
            return False
        
        if not root:
            return False

        return _traversal(root, targetSum)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
            遍历到叶节点，记录过程中的路径，如果总和满足题意，则存储路径
        """
        if not root:
            return []

        result = []

        def _traversal(root: TreeNode, path: List[int]):

            nonlocal targetSum, result

            path.append(root.val)

            # 判断是否到达叶节点
            if root.left == None and root.right == None:

                if sum(path) == targetSum:
                    # result.append[path]  这样写只会添加 path 中第一个元素
                    result.append(path[:])
            
            # 递归逻辑 
            if root.left:
                # leftPath = copy.deepcopy(path)
                # _traversal(root.left, leftPath)
                _traversal(root.left, path) 
                path.pop()  # 递归中 path 添加了 left 的值
            if root.right:
                # rightPath = copy.deepcopy(path)
                # _traversal(root.right, rightPath)
                _traversal(root.right, path)
                path.pop()
        
        _traversal(root, [])

        return result
