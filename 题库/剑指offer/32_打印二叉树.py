class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
from collections import deque

"""从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
"""

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        """层次遍历
        """
        if not root:
            return []
        
        ans = []
        que = deque([root])

        while que:
            node = que.popleft()
            ans.append(node.val)

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        
        return ans

"""从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        que = deque([root])

        while que:

            level, width = [], len(que)

            for _ in range(width):
                node = que.popleft()
                level.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            ans.append(level)

        return ans

"""
    请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
    第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
            本题有多种思路:
            1. 层次遍历 + 双端队列
                利用双端队列的两端皆可添加元素的特性，设打印列表（双端队列） tmp ，并规定：
                    奇数层 则添加至 tmp 尾部 ，
                    偶数层 则添加至 tmp 头部 。
            
            2. 层序遍历 + 双端队列（奇偶层逻辑分离）
                方法一代码简短、容易实现；但需要判断每个节点的所在层奇偶性，即冗余了 NN 次判断。
                通过将奇偶层逻辑拆分，可以消除冗余的判断

            3. 层序遍历 + 倒序
                此方法的优点是只用列表即可，无需其他数据结构。
                偶数层倒序： 若 res 的长度为 奇数 ，说明当前是偶数层，则对 tmp 执行 倒序 操作。
        """
        if not root:
            return []
        
        ans = []
        que = deque([root])

        while que:

            level, width = [], len(que)

            for _ in range(width):
                node = que.popleft()
                level.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if len(ans) % 2 == 1:
                # 当前层为偶数层，需要逆序
                level = level[::-1]

            ans.append(level)

        return ans