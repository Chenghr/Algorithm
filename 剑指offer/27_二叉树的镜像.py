"""
    请完成一个函数，输入一个二叉树，该函数输出它的镜像。
"""
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        """递归，每个交换每个节点的左右子树节点即可
        """
        if not root:
            return None
        
        root.left = self.mirrorTree(root.left)
        root.right = self.mirrorTree(root.right)

        root.left, root.right = root.right, root.left

        return root

    def mirrorTree(self, root: TreeNode) -> TreeNode:
        """迭代解法
            层次遍历，每次遇到一个节点将其左右节点交换，然后入队列，直到队列为空。
        """
        if not root:
            return None

        que = deque()
        que.append(root)

        while len(que) != 0:
            node = que.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return root 
        