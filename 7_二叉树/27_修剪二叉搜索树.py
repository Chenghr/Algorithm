"""
    题目描述:
        给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。
        通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
        修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 
        可以证明，存在唯一的答案。

        所以结果应当返回修剪好的二叉搜索树的新的根节点。
        注意，根节点可能会根据给定的边界发生改变。

    链接: https://leetcode-cn.com/problems/trim-a-binary-search-tree
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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
            注意题目要求保留树中元素的相对结构

            递归法: 
             - 确定递归函数的参数以及返回值
                通过递归函数的返回值来移除节点

             - 确定终止条件
                修剪的操作并不是在终止条件上进行的，所以就是遇到空节点返回就可以了。
            
             - 确定单层递归的逻辑
                1. 如果root（当前节点）的元素小于low的数值，那么应该递归右子树，并返回右子树符合条件的头结点;
                   左子树亦然；
                2. root 的元素满足要求，则递归处理左子树，结果赋给root->left，右子树亦然；
                3. 最后返回root节点; 
        """
        
        if not root:
            return None
        
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            # root 的 val 满足要求
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        
        return root
    
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
            迭代法求解;

            因为二叉搜索树的有序性，不需要使用栈模拟递归的过程。

            在剪枝的时候，可以分为三步:
                将root移动到[L, R] 范围内，注意是左闭右闭区间
                剪枝左子树
                剪枝右子树
        """
        if not root:
            return None
        
        # 锁定最终的 root 节点位置
        while (root != None and (root.val < low or root.val > high)):
            if root.val < low:
                root = root.right
            else:
                root = root.left
        
        # 处理左子树的值小于 low 的情况
        curNode = root

        while (curNode != None):
            # 一次修剪
            while (curNode.left and curNode.left.val < low):
                curNode.left = curNode.left.right
            
            curNode = curNode.left
        
        # 处理右子树的值大于 high 的情况
        curNode = root
        
        while (curNode != None):
            # 一次修剪
            while (curNode.right and curNode.right.val > high):
                curNode.right = curNode.right.left
            
            curNode = curNode.right
        
        return root
