"""
    题目描述:
        给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

        有效 二叉搜索树定义如下:
            节点的左子树只包含 小于 当前节点的数。
            节点的右子树只包含 大于 当前节点的数。
            所有左子树和右子树自身必须也是二叉搜索树。

    链接: https://leetcode-cn.com/problems/validate-binary-search-tree
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
            递归的判断每个 root 节点的左右节点的值是否满足条件，
            均满则返回 True ，有一个不满足则返回 False。

            注意陷阱:
                我们要比较的是 左子树所有节点小于中间节点，右子树所有节点大于中间节点，
                不能单纯的比较左节点小于中间节点，右节点大于中间节点就完事了

        """
        
        def _isValidBST_recurse(root: TreeNode, minVal: float, maxVal: float) -> bool:
            # 判断当前节点的值是否满足条件
            if root.val <= minVal or root.val >= maxVal:
                return False
            
            # 递归判断
            if root.left:
                validLeft = _isValidBST_recurse(root.left, minVal, min(maxVal, root.val))
            else:
                validLeft = True
            
            if root.right:
                validRight = _isValidBST_recurse(root.right, max(minVal, root.val), maxVal)
            else:
                validRight = True
            
            return validLeft & validRight
        
        
        return _isValidBST_recurse(root, -float('inf'), float('inf'))


    def isValidBST(self, root: TreeNode) -> bool:
        """
            上一个方法的改进: 采用中序遍历的顺序来遍历

            核心关注:
                中序遍历的 BST 树的数值是从小到大的，我们仅需要记录目前的最大值即可。
        """

        curMax = -float('inf')

        def _inorder_traverse(root: TreeNode) -> bool:
            nonlocal curMax

            if not root:
                return True
            
            valid_left = _inorder_traverse(root.left)

            if curMax < root.val:
                curMax = root.val
            else:
                return False
            
            valid_right = _inorder_traverse(root.right)

            return valid_left & valid_right
        
        return _inorder_traverse(root)


    def isValidBST(self, root: TreeNode) -> bool:
        """
            思路: 利用BST中序遍历的特性.
                 中序遍历输出的二叉搜索树节点的数值是有序序列

            对树进行中序遍历，判断输出的数组是否为有序序列
        """
        candidate_list = []

        def _inorder_traverse(root: TreeNode) -> None:
            nonlocal candidate_list

            if not root:
                return
            
            _inorder_traverse(root.left)  # 左
            candidate_list.append(root.val)  # 中
            _inorder_traverse(root.right)  # 右
        
        def _isOrdered(nums: list) -> bool:

            for i in range(1, len(nums)): 

                if nums[i] <= nums[i - 1]: 
                    # 注意: Leetcode定义二叉搜索树中不能有重复元素
                    return False

            return True
        
        _inorder_traverse(root)

        return _isOrdered(candidate_list)
