"""
    输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
    B是A的子结构， 即 A中有出现和B相同的结构和节点值。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return False
        
        if not self.isContain(A, B):
            # 以当前A节点为根节点，不包含B的结构，则向A的左右子树分别寻找
            return self.isContain(A.left) or self.isContain(A.right, B)
        else:
            # 以当前A节点为根节点，包含B的结构
            return True

    def isContain(self, nodeA: TreeNode, nodeB: TreeNode) -> bool:
        """以 nodeA 为根的树是否包含 nodeB, 且 nodeB 不全为空"""
        # 边界条件处理
        if not nodeB:
            # 遍历到空节点，则说明包含
            return True
        
        if not nodeA or nodeA.val != nodeB.val:
            return False
        
        # 单层递归逻辑
        left = self.isContain(nodeA.left, nodeB.left)
        right = self.isContain(nodeA.right, nodeB.right)

        return left and right  # 左右均包含，才真的包含
