"""
    给你二叉树的根结点 root ，请你将它展开为一个单链表：

    展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
    展开后的单链表应该与二叉树 先序遍历 顺序相同。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
            遍历的思路
                采用先序遍历的顺序；
                根据题意，需要记录前驱节点的信息，以及保留当前节点的右孩子节点（遍历过程中会被更改）。
        """
        def preOrderTraverse(root: TreeNode):
            nonlocal preNode

            if not root:
                return
            
            if preNode:
                preNode.left = None
                preNode.right = root
            preNode = root

            right = root.right          # 保留右子树信息
            preOrderTraverse(root.left)
            preOrderTraverse(right)
        
        preNode = None
        preOrderTraverse(root)
        return root   
    
    def flatten(self, root: TreeNode) -> None:
        """
            分解问题的思路
                
                flatten 定义: 输入节点 root，然后 root 为根的二叉树就会被拉平为一条链表

                对于一个节点 x，可以执行以下流程:
                1、先利用 flatten(x.left) 和 flatten(x.right) 将 x 的左右子树拉平。
                2、将 x 的右子树接到左子树下方，然后将整个左子树作为右子树。

        """
        if not root:
            return                 # flatten 函数没有返回值
        
        # 分别拉平左右子树
        self.flatten(root.left)
        self.flatten(root.right)

        right = root.right         # 暂存拉平的右子树
        root.right = root.left     # 更改左右子树布局
        root.left = None

        # 将右子树拼接到左子树末端
        node = root                # 避免左子树为空的情况，从 root 开始
        while node.right:
            node = node.right
        
        node.right = right

    def flatten(self, root: TreeNode) -> None:
        """
            遍历的思路 - 寻找前驱节点，
                对于当前节点，如果其左子节点不为空，则在其左子树中找到最右边的节点，作为前驱节点，
                将当前节点的右子节点赋给前驱节点的右子节点，
                然后将当前节点的左子节点赋给当前节点的右子节点，并将当前节点的左子节点设为空。
                
                对当前节点处理结束后，继续处理链表中的下一个节点，直到所有节点都处理结束。
        """
        curNode = root

        while curNode:
            if curNode.left:

                preNode = curNode.left          # 寻找前驱节点
                while preNode.right:
                    preNode = preNode.right

                preNode.right = curNode.right   # 节点关系转换
                curNode.right = curNode.left
                curNode.left = None
            
            curNode = curNode.right

        



