"""
    题目描述:
        给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

        一般来说，删除节点可分为两个步骤:
            首先找到需要删除的节点；
            如果找到了，删除它。
    
    进阶: 要求算法时间复杂度为 O(h)，h 为树的高度。

    链接: https://leetcode-cn.com/problems/delete-node-in-a-bst
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
            BST 的删除:
                1. 找到目标节点并删除；
                2. 维护删除后的树结构，保持 BST 不变
            
            寻找目标节点，有如下情况:
                1. 没找到要删除的节点，直接返回；
                2. 找到要删除的节点。
            
            对于要删除的节点，有如下情况:   
                1. 叶子节点
                    直接删除即可，返回 None
                2. 中间节点
                    a. 左右子树有一个为空，则直接返回非空的那个即可；
                    b. 左右子树均不为空，这时根据 BST 树的性质，应该将左子树放到右子树的最左下角
                       然后，返回右子树。
        """

        def _deleteNode(target: Optional[TreeNode]) -> Optional[TreeNode]:
            """对找到的目标节点进行删除操作"""
            # 叶节点，直接删除
            if target.left == None and target.right == None:
                return None

            # 中间节点
            if target.left == None:
                return target.right
            elif target.right == None:
                return target.left
            else:
                node = target.right

                while(node.left != None):
                    node = node.left
                
                node.left = target.left
                
                return target.right
        
        preNode = None

        def _findNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

            if not root:
                return None

            nonlocal preNode

            if root.val == key:
                return root
            elif root.val < key:
                preNode = root
                return _findNode(root.right, key)
            else:
                preNode = root
                return _findNode(root.left, key)
        
        # 寻找目标节点
        target = _findNode(root, key)

        if target == None:
            # 找不到目标节点
            return root

        if target == root:
            # 目标节点为根节点
            return _deleteNode(root)

        if preNode.left == target:
            preNode.left = _deleteNode(target)
        else:
            preNode.right = _deleteNode(target)
        
        return root