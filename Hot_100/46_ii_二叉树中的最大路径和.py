"""
    题目描述:
        路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
        同一个节点在一条路径序列中 至多出现一次 。
        该路径 至少包含一个 节点，且不一定经过根节点。
        路径和 是路径中各节点值的总和。

        给你一个二叉树的根节点 root ，返回其 最大路径和 。

    链接: https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
            难点在于理解题意和转化题意。
            1. "可以从任意节点出发, 到达任意节点"的路径, 一定是先上升 x 个节点, 
                到达顶点, 后下降 y 节点。
                我们可以通过枚举顶点的方式来枚举路径。
                
            2. 我们枚举顶点时, 可以把路径分拆成3部分: 左侧路径、右侧路径和顶点;
                以当前节点为顶点的路径中, 最大和为 两侧路径的最大和 + 节点的值。
                需要注意的是, 两侧路径也可能不选, 此时取 0。

            3. 如何求两侧路径最大和？ 看一个类似问题：求数组的最大子数组和。
                动态规划： dp[i] 代表以 nums[i] 为结尾的子数组的最大和。
                转移方程： dp[i] = max(dp[i-1], 0) + nums[i]。

            4. 在树上, 设 dp[C] 代表以当前节点为结尾的最大上升路径和, 
                则我们需要对节点的左右子树做一个选择, 有
                    dp[C] = max(max(dp[L], 0), max(dp[R], 0)) + C.val
                式中, C,L,R 分别代指 当前节点、左子节点、右子节点。
            
            5. 最后, 以当前节点为顶点的路径中, 最大的和为
                max(dp[L], 0) + max(dp[R], 0) + C.val。
                我们枚举顶点, 并记录最大答案。
            
            由于需要左右子树的最大路径和来处理本节点的，因此采用后序遍历；
        """

        maxSum = root.val  # 不可置为 0

        def postOrder(node: TreeNode):
            nonlocal maxSum

            if node == None:
                return 0
            
            maxLeftSum = max(postOrder(node.left), 0)
            maxRightSum = max(postOrder(node.right), 0)
            
            # 选择当前节点作为顶点的最大路径和
            curMaxSum = node.val + maxLeftSum + maxRightSum
            maxSum = max(maxSum, curMaxSum)

            # 当前节点作为一侧路径的最大路径和
            sideMaxSum = max(maxLeftSum, maxRightSum) + node.val

            return sideMaxSum
            
        postOrder(root)

        return maxSum