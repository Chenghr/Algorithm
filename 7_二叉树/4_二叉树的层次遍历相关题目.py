from types import resolve_bases
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
            题目描述:
                给你二叉树的根节点 root ，返回其节点值自底向上的层序遍历。 
                即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历。
            
            链接: https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
        """
        if root is None:
            return []

        result = []

        def traversal(root: TreeNode, depth: int):
            nonlocal result

            if len(result) == depth:
                result.append([])
            
            result[depth].append(root.val)

            if root.left is not None:
                traversal(root.left, depth+1)
            if root.right is not None:
                traversal(root.right, depth+1)
        
        traversal(root, 0)
        result.reverse()

        return result
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
            题目描述:
                给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

            链接: https://leetcode-cn.com/problems/binary-tree-right-side-view/
        """
        if root is None:
            return []
        
        result_level = []
        que = deque([(root, 0)])

        while (len(que) != 0):
            node, depth = que.popleft()

            if len(result_level) == depth:
                result_level.append([])

            result_level[depth].append(node.val)
            
            if node.left is not None:
                que.append((node.left, depth+1))
            if node.right is not None:
                que.append((node.right, depth+1))
        
        result = [level[-1] for level in result_level]
        
        return result

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
            题目描述:
                给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
            
            链接: https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
        """
        if root is None:
            return 0
        
        result_level = []
        que = deque([(root, 0)])

        while (len(que) != 0):
            node, depth = que.popleft()

            if len(result_level) == depth:
                result_level.append([])

            result_level[depth].append(node.val)
            
            if node.left is not None:
                que.append((node.left, depth+1))
            if node.right is not None:
                que.append((node.right, depth+1))
        
        result = []
        for level in result_level:
            sum = 0.0

            for num in level:
                sum += num

            result.append(sum / len(level))
        
        return result
    
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
            题目描述:
                给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
                树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
            
            链接: https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
        """
        if root is None:
            return []
        
        result = []
        que = deque([(root, 0)])
        
        while (len(que) != 0):
            node, depth = que.popleft()
            
            if len(result) == depth:
                result.append([])
            
            result[depth].append(node.val)

            if node.children is not None:
                for child in node.children:
                    que.append((child, depth+1))
        
        return result

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
            题目描述: 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

            链接: https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/
        """
        result = []

        def traversal(root: TreeNode, depth: int):
            if root is None:
                return 
            
            nonlocal result

            if len(result) == depth:
                result.append(root.val)
            else:
                result[depth] = max(result[depth], root.val)

            if root.left is not None:
                traversal(root.left, depth+1)
            if root.right is not None:
                traversal(root.right, depth+1)
        
        traversal(root, 0)

        return result
    