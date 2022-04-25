"""给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """常规二叉树
            p, q 一定在给定的二叉树中，
            因此如果 q 是 p 的子孙节点，我们在遇到 p 的时候直接返回也是可以拿到正确解的。
        """
        if not root:
            return None
        
        if root == p or root == q:  # 先序处理的原因：p、q一定在树中
            return root

        left = self.lowestCommonAncestor(root.left)
        right = self.lowestCommonAncestor(root.right)

        if left and right:  # 找到根节点
            return root
        
        return left if left else right  # 左右子树中返回非空的那个，如果均为空则返回的是 None
    
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """常规二叉树
            p, q 不一定在给定的二叉树中，不存在时返回 None
            需要全局判断 p, q 是否出现过
        """
        
        def findpq(root: TreeNode, p: TreeNode, q: TreeNode):
            nonlocal appearP, appearQ

            if not root:
                return None
        
            left = findpq(root.left, p, q)
            right = findpq(root.right, p, q)

            if left and right:
                return root

            # 后序处理
            if root == p or root == q:
                if root == p:
                    appearP = True
                if root == q:
                    appearQ = True
                return root
            
            return left if left else right

        appearP, appearQ = False, False

        ans = findpq(root, p, q)
        if appearP and appearQ:
            return ans

        return None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """二叉搜索树
            题目保证 p， q 在树内，可以减少一些边界条件的判断；
            利用二叉搜索树 左 < 中 < 右 的性质
        """
        def searchBST(root: TreeNode, p: TreeNode, q: TreeNode):
            if p.val <= root.val <= q.val:
                return root
            elif root.val < p.val:
                return searchBST(root.right, p, q)
            else:
                return searchBST(root.left, p, q)
        
        if p.val > q.val:
            p, q = q, p
        
        return searchBST(root, p, q)
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """二叉搜索树
            优化写法
        """
        ans = root

        while True:
            if ans.val < p.val and ans.val < q.val:
                ans = ans.right
            elif ans.val > p.val and ans.val > q.val:
                ans = ans.left
            else:
                break
        
        return ans
        