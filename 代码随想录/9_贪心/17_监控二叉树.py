"""
    题目描述:
        给定一个二叉树，我们在树的节点上安装摄像头。
        节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
        计算监控树的所有节点所需的最小摄像头数量。
    
    链接: https://leetcode-cn.com/problems/binary-tree-cameras/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        """
            要从下往上看;
            局部最优: 让叶子节点的父节点安摄像头，所用摄像头最少;
            整体最优: 全部摄像头数量所用最少.

            大体思路就是从低到上，先给叶子节点父节点放个摄像头，然后隔两个节点放一个摄像头，
            直至到二叉树头结点。

            二叉树的遍历:
                可以使用后序遍历也就是左右中的顺序，这样就可以在回溯的过程中从下到上进行推导了。
            
            如何隔两个节点放一个摄像头:
                每个节点有三个状态:
                - 该节点无覆盖: 0 表示
                - 本节点有摄像头: 1 表示
                - 本节点有覆盖: 2 表示
        """
        result = 0

        def traversal(root: TreeNode) -> int:
            if root == None:
                return 2
            
            left = traversal(root.left)  # 左
            right = traversal(root.right)  # 右

            # 中，本层处理逻辑
            # 三层 if 的判断顺序不能错
            if left == 2 and right == 2:
                return 0
            elif left == 0 or right == 0:
                # 安装摄像头
                nonlocal result
                result += 1
                return 1    
            elif left == 1 or right == 1:
                return 2

            return -1

        if traversal(root) == 0:
            # 判断根节点是否需要加装摄像头
            result += 1
        
        return result