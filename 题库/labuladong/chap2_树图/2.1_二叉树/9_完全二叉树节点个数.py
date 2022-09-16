"""
    给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

    完全二叉树 的定义如下：
        在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
        并且最下面一层的节点都集中在该层最左边的若干位置。
        若最底层为第 h 层，则该层包含 1~ 2h 个节点。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """普通二叉树的节点数统计；O(N)
        """
        if not root:
            return 0
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def countNodes(self, root: TreeNode) -> int:
        """完全二叉树的节点统计；O(logN * logN)
            分解问题 + 后序遍历 + 利用满二叉树的性质；
            （完全二叉树必有部分子树为满二叉树）
        """
        if not root:
            return 0

        # 判断当前树是不是满二叉树
        leftDepth, left = 0, root.left
        while left:
            leftDepth += 1
            left = left.left
        
        rightDepth, right = 0, root.right
        while right:
            rightDepth += 1
            right = right.right
        
        if leftDepth == rightDepth:         # 当前树是完全二叉树
            return (1 << (leftDepth + 1)) - 1
        
        # 非满二叉树的时候，采用递归处理的方式。
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


