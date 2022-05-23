"""
    给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。

    每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。
        二叉搜索树的定义如下：

        任意节点的左子树中的键值都 小于 此节点的键值。
        任意节点的右子树中的键值都 大于 此节点的键值。
        任意节点的左子树和右子树都是二叉搜索树。
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        """
            1. 判断子树是否为二叉搜索树；
            2. 在二叉搜索树中选择键值最大的返回。

            遍历的解决思路，后序遍历；
            返回三元组（子树中最小值，子树中最大值，子树键值和（非二叉搜索树返回-1））

            当前子树为二叉搜索树:
                1. 左右子树均为二叉搜索树；
                2. 当前节点值大于左子树返回最大值，小于右子树返回最小值
        """
        
        def postOrder(root: TreeNode):
            """返回 [子树中最小值，子树中最大值，子树键值和（非二叉搜索树返回float('inf')）]
            """
            nonlocal maxBstSum

            if not root:
                return [float('inf'), -float('inf') , 0]

            left = postOrder(root.left)
            right = postOrder(root.right)

            if left[-1] == float('inf') or right[-1] == float('inf') or root.val <= left[1] or root.val >= right[0]:
                # 当前子树无法构成二叉搜索树，向上也不会再构成了
                return [float('inf'), -float('inf') , float('inf')]

            # 当前子树为二叉搜索子树
            bstSum = left[-1] + right[-1] + root.val
            minBstVal = root.val if left[0] == float('inf') else left[0]
            maxBstVal = root.val if right[1] == -float('inf') else right[1]

            maxBstSum = max(maxBstSum, bstSum)

            return [minBstVal, maxBstVal, bstSum]
            
        maxBstSum = 0
        postOrder(root)
        return maxBstSum
