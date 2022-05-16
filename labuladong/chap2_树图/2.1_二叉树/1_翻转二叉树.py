"""给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """遍历的思路解决问题；
            对于遍历顺序不具备敏感性，就采用先序遍历解决。
        """
        def reverse(root: TreeNode):
            if not root:
                return

            root.left, root.right = root.right, root.left
            reverse(root.left)
            reverse(root.right)
        
        reverse(root)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        """分解问题的思路解决问题；
        """
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left
        return root