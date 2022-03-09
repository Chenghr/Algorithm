from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
            题目描述:
                给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点；
                填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
                初始状态下，所有 next 指针都被设置为 NULL。

            进阶:
                你只能使用常量级额外空间。
                使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

            链接: https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
        """
        if root is None:
            return root
        
        def traversal_level(root: 'Optional[Node]'):
            if root.left is not None and root.right is not None:
                root.left.next = root.right
            
                if root.next is not None:
                    root.right.next = root.next.left
            
            if root.left is not None:
                traversal_level(root.left)
            if root.right is not None:
                traversal_level(root.right)

        traversal_level(root)
        
        return root

    def connect_graceful(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
            题解: https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-2-4/

            几个注意点:
                - 当第 N 层节点的 next 指针全部建立完成后，移至第 N 层，建立第 N+1 层节点的 next 指针。
                - 遍历某一层的节点时，这层节点的 \text{next}next 指针已经建立。
                  因此我们只需要知道这一层的最左节点，就可以按照链表方式遍历，不需要使用队列。
        """

        if not root:
            return root
        
        leftmost = root

        while leftmost.left:

            # 遍历这一层节点组成的链表，为下一层的节点更新
            head = leftmost

            while head:
                # 本身的孩子节点连接
                head.left.next = head.right

                # 跨越子树的孩子节点相连
                if head.next:
                    head.right.next = head.next.left
                
                # 向后连接指针
                head = head.next
            
            # 去下一层的最左的节点
            leftmost = leftmost.left
        
        return root
    
    def connect2(self, root: 'Node') -> 'Node':
        """
            题目描述:
                给定一个二叉树, 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。
                如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
                初始状态下，所有 next 指针都被设置为 NULL。
            
            进阶:
                你只能使用常量级额外空间。
                使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
            
            链接: https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
        """
        if not root:
            return root
        
        leftmost = root
        
        while leftmost:
            # 当前层遍历的起点
            head = leftmost

            # 记录下一层的起点，以及下一层连接上的最后一个节点
            leftmost_nextlevel, pre = None, None

            while head:
                if head.left is not None:
                    # 找下一层的起点
                    if not leftmost_nextlevel:
                        leftmost_nextlevel = head.left

                    if not pre:
                        # 初始化pre节点
                        pre = head.left
                    else:
                        # 更新pre节点
                        pre.next = head.left
                        pre = head.left
                    
                if head.right is not None:
                    # 找下一层的起点
                    if not leftmost_nextlevel:
                        leftmost_nextlevel = head.right

                    if not pre:
                        # 初始化pre节点
                        pre = head.right
                    else:
                        # 更新pre节点
                        pre.next = head.right
                        pre = head.right
                    
                head = head.next
            
            leftmost = leftmost_nextlevel
        
        return root

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
            题目描述:
                给定一个二叉树，找出其最大深度。
                二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
                说明: 叶子节点是指没有子节点的节点。
            
            链接: https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
        """
        if not root:
            return 0

        maxdepth = 1

        def traversal(root: Optional[TreeNode], depth: int):

            nonlocal maxdepth
            maxdepth = max(maxdepth, depth)
            
            if root.left is not None:
                traversal(root.left, depth+1)
            if root.right is not None:
                traversal(root.right, depth+1)
        
        traversal(root, 1)

        return maxdepth
    
    def minDepth(self, root: TreeNode) -> int:
        """
            题目描述:
                给定一个二叉树，找出其最小深度。
                最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
                说明: 叶子节点是指没有子节点的节点。
            
            链接: https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
        """
        if not root:
            return 0
        
        que = deque([(root, 1)])

        while len(que) != 0:
            node, depth = que.popleft()

            if node.left == None and node.right == None:
                return depth
            
            if node.left:
                que.append((node.left, depth+1))
            if node.right:
                que.append((node.right, depth+1))
        
        return 0
