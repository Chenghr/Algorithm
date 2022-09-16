"""
    给定一棵二叉搜索树，请找出其中第 k 大的节点的值。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """中序遍历, 第k大，因此先遍历右子树再遍历左子树

            复杂度分析：
                时间复杂度 O(N): 当树退化为链表时（全部为右子节点），无论 k 的值大小，递归深度都为 N ，占用 O(N) 时间。
                空间复杂度 O(N): 当树退化为链表时（全部为右子节点），系统使用 O(N)大小的栈空间。
        """
        ans = None

        def inOrder(root: TreeNode):
            nonlocal ans, k

            if not root:
                return 
            
            inOrder(root.right)

            k -= 1
            if k == 0:
                ans = root.val
            
            if k:  # 剪枝
                inOrder(root.left)

        inOrder(root)

        if k > 0:
            # 说明 k 大于树中节点数目，找不到这样的解
            return float('inf')

        return ans  # 本题保证了一定有解，否则要对 ans 做判断

    def kthLargest(self, root: TreeNode, k: int) -> int:
        """中序遍历, 非迭代"""
        node, stack = root, []

        while stack or node:
            if node:
                stack.append(node)
                node = node.right  # 右子树一直入栈
            else:
                node = stack.pop()
                k -= 1

                if k == 0:
                    return node.val

                node = node.left 

        return -1