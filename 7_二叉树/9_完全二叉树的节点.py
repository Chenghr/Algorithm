"""
    题目描述:
        给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

        完全二叉树 的定义如下:
            在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。
            若最底层为第 h 层，则该层包含 1~ 2^h 个节点。
    
    进阶: 遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？

    链接: https://leetcode-cn.com/problems/count-complete-tree-nodes
"""

"""
    暴力求解:
        遍历整棵树，记录节点数目即可。

    利用完全二叉树的性质:
        完全二叉树只有两种情况，情况一: 就是满二叉树，情况二: 最后一层叶子节点没有满。

        - 情况一:
            可以直接用 2^树深度 - 1 来计算，注意这里根节点深度为1。

        - 情况二:
            分别递归左孩子，和右孩子，递归到某一深度一定会有左孩子或者右孩子为满二叉树，
            然后依然可以按照情况一来计算。

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
    def countNodes(self, root: TreeNode) -> int:

        if root == None:
            return 0
        
        left_depth, right_depth = 0, 0
        left_node, right_node = root.left, root.right

        # 最左侧深度
        while (left_node):
            left_node = left_node.left
            left_depth += 1
        
        # 最右侧深度
        while (right_node):
            right_node = right_node.right
            right_depth += 1

        if left_depth == right_depth:
            # 满二叉树
            return (1 << (left_depth+1)) - 1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1 
        
