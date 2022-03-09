"""
    题目描述:
        给你一个二叉树的根节点 root ， 检查它是否轴对称。
    
    进阶: 你可以运用递归和迭代两种方法解决这个问题吗？

    链接: https://leetcode-cn.com/problems/symmetric-tree/
"""

from typing import List, Optional
from collections import deque

import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSymmetric_violet(self, root: TreeNode) -> bool:
        """
            思路（暴力思想）:
                将一棵二叉树反转获得一棵新的二叉树；
                遍历这两棵二叉树，如果完全相同，则镜像对称，否则不对称。
        """

        def invertTree(self, root: TreeNode) -> TreeNode:
            if root == None:
                return root
            
            queue_ = deque([root])

            while queue_:
                cur = queue_.popleft()

                if cur.left:
                    queue_.append(cur.left)
                if cur.right:
                    queue_.append(cur.right)
                
                cur.left, cur.right = cur.right, cur.left
            
            return root

        reverse_root = copy.deepcopy(root)
        reverse_root = invertTree(reverse_root)

        que1 = deque([root])
        que2 = deque([reverse_root])

        while que1 and que2:
            cur1 = que1.popleft()
            cur2 = que2.popleft()

            if cur1 == None and cur2 != None:
                return False
            if cur1 != None and cur2 == None:
                return False
            if cur1 != None and cur2 != None:
                if cur1.val != cur2.val:
                    return False
            
            if cur1:
                que1.append(cur1.left)
                que1.append(cur1.right)
            if cur2:
                que2.append(cur2.left)
                que2.append(cur2.right)
        
        if len(que1) == 0 and len(que2) == 0:
            return True

        return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        """
            思路:
                判断对称二叉树要比较的不是左右节点，要比较的是根节点的左子树与右子树是不是相互翻转的；
                进一步的是，两个子树的里侧和外侧的元素是否相等。
            
            具体:
                本题遍历只能是“后序遍历”，因为我们要通过递归函数的返回值来判断两个子树的内侧节点和外侧节点是否相等。
                正是因为要遍历两棵树而且要比较内侧和外侧节点，所以准确的来说是一个树的遍历顺序是左右中，一个树的遍历顺序是右左中。
        """

        def compare(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:

            # 左右节点是否为 None 的判断与解决
            if left == None and right != None:
                return False
            elif left != None and right == None:
                return False
            elif left == None and right == None:
                return True

            # 左右节点的值的比较处理
            if left.val != right.val:
                return False

            # 递归处理
            outside = compare(left.left, right.right)  # 左子树: 左， 右子树：右
            inside = compare(left.right, right.left)  # 左子树: 右， 右子树: 左

            # 返回值判断
            isSame = outside & inside

            return isSame
        
        if not root:
            return True
        
        return compare(root.left, root.right)