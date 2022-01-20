"""
    题目描述:
        给你一个含重复值的二叉搜索树（BST）的根节点 root ，
        找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
        如果树中有不止一个众数，可以按 任意顺序 返回。

    链接: https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        """
            求解思路:
                中序遍历 BST 树，然后在数组中获取众数。
                利用 BST 中序有序的特点
            
            本题可以引出有序数组如何有效求解中数的问题
        """
        result = []
        
        preNode, count, maxCount = None, 0, 0

        def _traverse_inorder(root: TreeNode):
            if not root:
                return 

            # 左
            _traverse_inorder(root.left) 
            
            # 中
            nonlocal preNode, count, maxCount, result

            # 第一个节点
            if preNode is None:
                preNode = root
                count = 1
            # 与前一个节点数值相同
            elif preNode.val == root.val:
                count += 1
            # 与前一个节点数值不同
            else:
                count = 1
            
            # 判断当前计数与最大计数的关系
            if count == maxCount:
                result.append(root.val)
            elif count > maxCount:
                maxCount = count
                result = [root.val]  # 清空之前的最大值
            
            # 更新节点
            preNode = root

            # 右
            _traverse_inorder(root.right)

        _traverse_inorder(root)

        return result