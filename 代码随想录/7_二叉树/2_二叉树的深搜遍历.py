"""
    题目描述:
        给你二叉树的根节点 root ，返回它节点值的 前序、中序、后序 遍历。

    链接:
        https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
        https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
        https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
        
"""

"""
    递归算法的三要素:
        1. 确定递归函数的参数和返回值;
        2. 确定终止条件;
        3. 确定单层递归的逻辑.

    使用迭代法（栈）核心在于两个操作:
        1. 处理: 将元素放进 result 数组中
        2. 访问: 遍历节点
    
    使用标记法可以统一三种访问顺序的代码格式，值得记忆.
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traversal(root: Optional[TreeNode]):
            if root is None:
                # 终止条件
                return

            # 单层递归的逻辑
            nonlocal result

            result.append(root.val)
            traversal(root.left)
            traversal(root.right)
        
        traversal(root)

        return result

    def preorderTraversal_stack(self, root: Optional[TreeNode]) -> List[int]:
        """前序遍历的顺序: 中左右;
            先访问的元素是中间节点，要处理的元素也是中间节点
            要访问的元素和要处理的元素顺序是一致的，都是中间节点。
        """
        if not root:
            return []

        stack, ans = [root], []

        while stack:
            node = stack.pop()

            ans.append(node.val)
            if node.right:    # 栈的性质，右节点先入栈
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        ans.reverse()
        return ans
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        curNode, stack, ans = root, [], []
        while curNode or stack:
            if curNode:
                stack.append(curNode)
                curNode = curNode.left
            else:
                node = stack.pop()
                ans.append(node.val)
                curNode = node.right
        
        return ans

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traversal(root: Optional[TreeNode]):
            if root is None:
                return 
            
            nonlocal result

            traversal(root.left)
            result.append(root.val)
            traversal(root.right)
        
        traversal(root)

        return result

    def inorderTraversal_stack(self, root: Optional[TreeNode]) -> List[int]:
        """中序遍历: 左中右;
            先访问的是二叉树顶部的节点，然后一层一层向下访问，直到到达树左面的最底部，再开始处理节点
            处理顺序和访问顺序是不一致的;

            处理方法: 借用指针的遍历来帮助访问节点，栈则用来处理节点上的元素.
        """
        if root is None:
            return []
        
        result = []
        stack, node = [], root

        while (node is not None or len(stack) != 0):
            if node is not None:
                # 使用指针访问节点，直到最底层
                stack.append(node)
                node = node.left  # 左
            else:
                # 从栈顶弹出要处理的数据
                node = stack.pop()

                result.append(node.val)  # 中

                node = node.right  # 右
        
        return result

    def inorderTraversal_stack_tag(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack, ans = [root], []

        while stack:
            node = stack.pop()

            if node:                            # 非标记节点，压栈
                if node.right:
                    stack.append(node.right)
                
                stack.append(None)              # 添加标记节点
                stack.append(node)

                if node.left:
                    stack.append(node.left)
            else:                               # 遇到标记节点，处理下个节点
                node = stack.pop()
                ans.append(node.val)
        
        return ans

    def inorderTraversal_stack_tag(self, root: Optional[TreeNode]) -> List[int]:
        """新的处理方法:
            将访问的节点放入栈中，把要处理的节点也放入栈中但是要做标记;
            要处理(输出值到result数组中)的节点放入栈之后，紧接着放入一个空指针作为标记.
        """
        if root is None:
            return []
        
        result = []
        stack = [root]

        while (len(stack) != 0):
            node = stack.pop()

            if node is not None:
                # 遇到栈中的非空元素，按照访问顺序，处理左右节点与中间节点
                if node.right is not None:
                    stack.append(node.right)

                stack.append(node)
                stack.append(None)

                if node.left is not None:
                    stack.append(node.left)
            
            else:
                # 遇到栈中的空元素，则对下一个元素进行读取处理
                node = stack.pop()
                result.append(node.val)
        
        return result

                

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traversal(root: Optional[TreeNode]):
            if root is None:
                return 
            
            nonlocal result

            traversal(root.left)
            traversal(root.right)
            result.append(root.val)
        
        traversal(root)

        return result

    def postorderTraversal_stack(self, root: Optional[TreeNode]) -> List[int]:
        """先序: 中左右 -> 微调: 中右左 -> 逆序: 左右中，即后序
        """
        if root is None:
            return []
        
        result = []
        stack = [root]

        while (len(stack) != 0):
            node = stack.pop()
            
            result.append(node.val)

            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        
        result.reverse()

        return result

    
