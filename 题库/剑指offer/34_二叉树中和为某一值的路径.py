"""
    给你二叉树的根节点 root 和一个整数目标和 targetSum ，
    找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

    叶子节点 是指没有子节点的节点。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        """
            先根遍历的优化写法
        """
        path, ans = [], []

        def traverse(root: TreeNode, target: int):
            if not root:
                return
            
            path.append(root.val)
            target -= root.val

            if not root.left and not root.right and target == 0:
                # 判断是否到达了终点，注意这里不能return，因为还要对 path 回溯
                ans.append(path[:])
            
            traverse(root.left, target)
            traverse(root.right, target)

            path.pop()  # target 仅在本函数内发生变化，不用回溯

        traverse(root, target)
        return ans

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        """
            从根节点到叶节点的路径和，则采用先根遍历
        """
        if not root:
            return []
        
        path, ans = [], []
        def traverse(root: TreeNode):
            nonlocal path, target, ans

            if root.left == None and root.right == None:  # 叶子节点
                path.append(root.val)

                if sum(path) == target:
                   ans.append(path[:])

                path.pop()
                return
            
            path.append(root.val)

            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            
            path.pop()
        
        traverse(root)
        return ans
