"""
    题目描述:
        小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
        除了 root 之外，每栋房子有且只有一个“父“房子与之相连。
        一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 
        如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

        给定二叉树的 root 。
        返回在不触动警报的情况下，小偷能够盗取的最高金额 。

    链接: https://leetcode-cn.com/problems/house-robber-iii
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
            树形dp；
            在树上遍历，使用递归；融合 dp，步骤如下:

            1. 确定递归函数的参数和返回值:
                求一个节点 偷与不偷的两个状态所得到的金钱，那么返回值就是一个长度为2的数组，即为 dp 数组；

            2. 确定终止条件:
                遇到空节点的话，很明显，无论偷还是不偷都是0，返回 [0, 0]，也是 dp 数组的初始化；

            3. 确定遍历顺序:
                使用后序遍历。 因为通过递归函数的返回值来做下一步计算。

            4. 确定单层递归的逻辑:
                如果是偷当前节点，那么左右孩子就不能偷:
                    val1 = cur->val + left[0] + right[0]; 

                如果不偷当前节点，那么左右孩子就可以偷，至于到底偷不偷一定是选一个最大的，所以:
                    val2 = max(left[0], left[1]) + max(right[0], right[1]);
                
                当前节点的状态就是{val2, val1}; 即: {不偷当前节点得到的最大金钱，偷当前节点得到的最大金钱}

            5. 举例推导dp数组
        """
        
        def traversal_recurse(root: TreeNode):
            if not root:
                # dp 初始化
                return [0, 0]
            
            # 左
            left = traversal_recurse(root.left) 
            
            # 右
            right = traversal_recurse(root.right)
            
            # 中
            val_free = max(left[0], left[1]) + max(right[0], right[1])  # 本层不偷
            val_steal = root.val + left[0] + right[0]  # 本层偷

            return [val_free, val_steal]

        result = traversal_recurse(root)

        return max(result[0], result[1])
            
    def rob(self, root: TreeNode) -> int:
        """
            暴力搜索 + 部分优化: 记忆化递归
        """
        memory = {}

        def traversal_recurse(root: TreeNode) -> int:
            nonlocal memory

            if not root:
                return 0
            
            if not root.left and not root.right:
                return root.val
            
            if root in memory:
                return memory[root]
            
            # 偷父节点
            val_steal = root.val
            if root.left:
                val_steal += traversal_recurse(root.left.left) + traversal_recurse(root.left.right)
            if root.right:
                val_steal += traversal_recurse(root.right.left) + traversal_recurse(root.right.right)
            
            # 不偷父节点
            val_free = traversal_recurse(root.left) + traversal_recurse(root.right)

            memory[root] = max(val_steal, val_free)

            return max(val_free, val_steal)
        
        return traversal_recurse(root)