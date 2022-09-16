"""
    题目描述:
        给定一棵二叉树，你需要计算它的直径长度。
        一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
        这条路径可能穿过也可能不穿过根结点。
    
    链接: https://leetcode-cn.com/problems/diameter-of-binary-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
            后续遍历；
            
            路径的长度为该路径经过的节点数减一，
            所以求直径（即求路径长度的最大值）等效于求路径经过节点数的最大值减一。

            任意一条路径均可以被看作由某个节点为起点，从其左儿子和右儿子向下遍历的路径拼接得到。
        """
        maxLength = 0

        def traverse(root: TreeNode):
            nonlocal maxLength

            if not root.left and not root.right:
                # 到达叶节点
                return 1
            
            # 左右子树的最长边长
            left = traverse(root.left) if root.left else 0
            right = traverse(root.right) if root.right else 0

            # 以当前节点作为中转节点
            curLength = left + right
            maxLength = max(maxLength, curLength)

            return max(left, right) + 1
        
        traverse(root)

        return maxLength