"""
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
    如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
"""

from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """单调栈解法
            https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/
        """
        stack, root = [], float('inf')
        # stack 中存储值递增的节点

        for i in range(len(postorder)):
            # 逆序遍历
            if postorder[i] > root:
                return False  # 根节点一定大于子节点
            
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()  # 持续出栈，且更新根节点
            
            stack.append(postorder[i])
        
        return True

    def verifyPostorder(self, postorder: List[int]) -> bool:
        """递归重写
        """
        def recur(left, right):
            if left >= right:
                return True
            
            i = left
            while postorder[i] < postorder[right]:  # 找到第一个大于根节点的下标
                i += 1
            
            middle = i  # 前半部分为左子树
            while postorder[i] > postorder[right]:  # 后半部分要满足均大于 root
                i += 1  # 注意这里不用边界判断，right类似于哨兵
            
            return i == right and recur(left, middle-1) and recur(middle, right-1)
        
        return recur(0, len(postorder)-1)

    def verifyPostorder(self, postorder: List[int]) -> bool:
        """
            利用二叉搜索树的性质，list 中最后一个数为根节点，
            找到第一个大于根节点的数的下标，之前的数都小于 root，之后的数都大于 root，
            再递归判断两个子序列是否满足，均满足则返回 true
        """
        if len(postorder) == 0 or len(postorder) == 1:
            return True
        
        root = postorder[-1]
        leftIndex, rightIndex = -1, len(postorder)-1

        index = len(postorder)-2
        while index >= 0:  # 从右向左找第一个小于 root 的下标
            if postorder[index] < root:
                leftIndex = index
                break
            index -= 1
        
        index = 0
        while index < len(postorder)-1:  # 从左向右找第一个大于 root 的下标
            if postorder[index] > root:
                rightIndex = index
                break
            index += 1
        
        if leftIndex > rightIndex:
            return False
        
        left = self.verifyPostorder(postorder[:leftIndex+1])
        right = self.verifyPostorder(postorder[rightIndex: len(postorder)-1])

        return left and right