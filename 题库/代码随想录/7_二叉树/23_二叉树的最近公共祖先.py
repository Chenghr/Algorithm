"""
    题目描述:   
        给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
        最近公共祖先的定义为:
            对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大
            （一个节点也可以是它自己的祖先）。

    提示:
        树中节点数目在范围 [2, 105] 内。
        -109 <= Node.val <= 109
        所有 Node.val 互不相同 。
        p != q
        p 和 q 均存在于给定的二叉树中。


    链接: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def construcTree(self, nums):
        nodes = []

        for val in nums:
            if val == 'null':
                nodes.append(None)
            else:
                nodes.append(TreeNode(val))
        
        for i in range(0, int(len(nodes)/2)):
            if (2*i + 1) < len(nodes):
                nodes[i].left = nodes[2*i + 1]
            if (2*i + 2) < len(nodes):
                nodes[i].right = nodes[2*i + 2]
        
        return nodes
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            中序遍历递归，记录节点的路径；遍历 p、q 路径的最长相同节点，即为所求祖先
        """
        path_p, path_q = [], []

        def _traverse(root: TreeNode, path: List[TreeNode]):
            nonlocal path_p, path_q

            if not root:
                return None

            # 中
            path.append(root)

            # 到达目标节点之一
            if root == p:
                path_p = path.copy()
            elif root == q:
                path_q = path.copy()
            
            # 左
            if root.left:
                _traverse(root.left, path)
                path.pop()  # 回溯
            
            # 右
            if root.right:
                _traverse(root.right, path)
                path.pop()

        _traverse(root, [])

        for i, node in enumerate(path_p):
            if i >= len(path_q) or node != path_q[i]:
                return path_p[i-1]
        
        return path_p[-1]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            题解思路:
                根据公共祖先的定义，如果找到一个节点，发现左子树出现结点p，右子树出现节点q，
                或者 左子树出现结点q，右子树出现节点p，那么该节点就是节点p和q的最近公共祖先。

                进一步想到自底向上查找，找到公共祖先

                自底向上查找 -> 后续遍历，回溯的过程就是从底向上遍历节点。
            
            递归三部曲:
             - 确定递归函数返回值以及参数:
                1. 返回值: 遇到 p、q 则返回，返回值不为空说明找到了 p 或者 q
                2. 参数: root, p, q
            
             - 确定终止条件:
                如果找到了 节点p或者q，或者遇到空节点，就返回。
                
             - 确定单层递归逻辑:
                递归处理左右子树，记录返回值为 left, right；
                    如果返回值都不为空，则 root 为最近公共节点；
                    left 为空，right 不为空，返回 right；反之亦然。
                    left, right 均为空，返回空即可。
        """
        # 终止条件
        if root == p or root == q or root == None:
            return root
        
        # 单层递归逻辑，后序遍历
        # 左，右
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 中
        if left != None and right != None:
            return root
        
        if left == None and right != None:
            return right
        elif left != None and right == None:
            return left
        else:
            return None


### Test ###

tree = Solution()
# nodes = tree.construcTree([3,5,1,6,2,0,8,'null','null',7,4])
nodes = tree.construcTree([1,2])
root = nodes[0]
# p = nodes[1]
# q = nodes[10]
p = nodes[1]
q = nodes[0]
result = tree.lowestCommonAncestor(root, p, q)
print(result.val)