"""
    题目描述:
        给你二叉树的根结点 root ，请你将它展开为一个单链表：
            展开后的单链表应该同样使用 TreeNode ，
            其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
            展开后的单链表应该与二叉树 先序遍历 顺序相同。

    进阶: 你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
    链接: https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
""" 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
            Do not return anything, modify root in-place instead.
            前序遍历；存储路径上的节点在list中，然后在list中处理节点
        """
    
        path = []

        def preOrderTraverse(node: TreeNode):
            if node:
                path.append(node)

                if node.left:
                    preOrderTraverse(node.left)
                if node.right:
                    preOrderTraverse(node.right)
        
        preOrderTraverse(root)

        for i in range(1, len(path)):
            pre, cur = path[i-1], path[i]
            pre.left = None
            pre.right = cur
        
        return root
    
    def flatten(self, root: TreeNode) -> None:
        """
            进阶: O(1)的时间复杂度实现
            借助先序遍历的非递归实现达到；栈中元素出栈；右指针指向栈顶元素即可
        """
        if not root:
            return

        stack = [root]

        while len(stack) != 0:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            node.left = None
            if len(stack) != 0:
                node.right = stack[-1]  # 防止最后一个元素出栈后栈为空
        
        return 