
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
            根据一棵树的中序遍历与后序遍历构造二叉树。
    
            注意: 你可以假设树中没有重复的元素。

            链接: https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
        """
        if len(inorder) == 0:
            return None

        # 递归终点，叶节点
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        # 中间节点
        rootVal = postorder[-1]
        leftIdx = inorder.index(rootVal)  # 获取第一个匹配到 rootVal 值的下标

        root = TreeNode(rootVal)
        root.left = self.buildTree(inorder[:leftIdx], postorder[:leftIdx])
        root.right = self.buildTree(inorder[leftIdx+1:], postorder[leftIdx:-1])

        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
            给定一棵树的前序遍历 preorder 与中序遍历 inorder。请构造二叉树并返回其根节点。
    
            注意: 你可以假设树中没有重复的元素。

            链接: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
        """
        if len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])

        # 递归终点，叶节点
        if len(inorder) == 1:
            return root
        
        # 中间节点
        leftIdx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:leftIdx+1], inorder[:leftIdx])
        root.right = self.buildTree(preorder[leftIdx+1:], inorder[leftIdx+1:])
        
        return root
        


            