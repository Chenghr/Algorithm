"""
    题目描述:
        给定一个二叉树的根节点 root ，和一个整数 targetSum ，
        求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

        路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

    链接: https://leetcode-cn.com/problems/path-sum-iii
"""

from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
            穷举法，穷举所有的可能，访问每一个节点node，检测以node为起始节点且向下延伸的路径有多少种；
            先根遍历；
            rootSum(p, targetSum): 以当前节点 p 为目标路径的起点，递归向下搜索；
        """
        def rootSum(root: TreeNode, targetSum):
            if not root:
                return 0
            
            ans = 1 if root.val == targetSum else 0
            
            ans += rootSum(root.left, targetSum-root.val)
            ans += rootSum(root.right, targetSum-root.val)

            return ans
        
        ans = rootSum(root, targetSum)  # 以 root 为起点
        ans += self.pathSum(root.left, targetSum)  # 以 root.left 作为备选起点
        ans += self.pathSum(root.right, targetSum)  # 以 root.right 作为备选起点

        return ans
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
            利用前缀和减少计算；

            记录根节点到当前节点p的路径上除当前节点以外所有节点的前缀和；
            在已保存的路径前缀和中查找是否存在前缀和刚好等于当前节点到根节点的前缀和 curr 减去 targetSum。
        """
        prefix = defaultdict(int)
        prefix[0] = 1

        def preOrder(root, pathSum):
            if not root:
                return 0
            
            ans = 0

            pathSum += root.val
            ans += prefix[pathSum - targetSum]

            prefix[pathSum] += 1

            ans += preOrder(root.left, pathSum)
            ans += preOrder(root.right, pathSum)

            prefix[pathSum] -= 1  # 回溯

            return ans
        
        return preOrder(root, 0)
