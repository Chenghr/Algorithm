"""
    给定一棵二叉树 root，返回所有重复的子树。
    对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。、
    如果两棵树具有相同的结构和相同的结点值，则它们是重复的。
"""

from typing import Optional, List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
            遍历问题的思路；

            子树的唯一标记: 序列化
            寻找重复子树: 哈希存储序列
            子树判断: 后序遍历
        """
        def postOrder(root: TreeNode):
            """返回后序遍历的子树序列。
            """
            nonlocal dic, ans

            if not root:
                return '#,'
            
            left = postOrder(root.left)
            right = postOrder(root.right)

            # 以当前节点为根节点的子树序列数据
            subTree = left + right + str(root.val) + ','

            dic[subTree] += 1
            if dic[subTree] == 2:  # 第一次重复出现，避免多次添加
                ans.append(root)

            return subTree
        
        dic, ans = defaultdict(int), []
        postOrder(root)
        return ans
        