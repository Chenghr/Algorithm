class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
    输入一棵二叉树的根节点，求该树的深度。
    从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """后序遍历，不传递参数"""
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root: TreeNode) -> int:
        """传递参数，先序遍历"""
        def dfs(root: TreeNode, depth: int):
            nonlocal maxDepth

            if not root.left and not root.right:
                maxDepth = max(maxDepth, depth)
                return
            
            if root.left:
                dfs(root.left, depth+1)
            if root.right:
                dfs(root.right, depth+1)
        
        if not root:
            return 0
        
        maxDepth = 0
        dfs(root, 1)
        return maxDepth

"""
    输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
    如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
"""

class Solution:
    def treeConstruct(self, vals):
        nodes = []

        for val in vals:
            if val != -1:
                nodes.append(TreeNode(val))
            else:
                nodes.append(None)
        
        for i in range(int(len(nodes)/2)+1):
            if 2*i+1 < len(nodes):
                nodes[i].left = nodes[2*i+1]
            if 2*i+2 < len(nodes):
                nodes[i].right = nodes[2*i+2]
        
        return nodes[0]

    def isBalanced(self, root: TreeNode) -> bool:
        def postOrder(root: TreeNode):
            if not root:
                return 0
            
            leftDepth = postOrder(root.left)
            rightDepth = postOrder(root.right)

            if leftDepth > -1 and rightDepth > -1 and abs(leftDepth - rightDepth) <= 1:
                return max(leftDepth, rightDepth) + 1

            return -1
        
        if not root:
            return True
        
        if postOrder(root) > -1:
            return True
        return False