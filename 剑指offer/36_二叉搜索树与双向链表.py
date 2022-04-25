"""
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
    要求不能创建任何新的节点，只能调整树中节点指针的指向。
"""

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """遍历时修改，记录中序遍历的 pre 指针以及整体的 head 指针即可"""
        def inorder(root: Node):
            nonlocal pre, head

            if not root:
                return None

            inorder(root.left)

            if not pre:  # 核心逻辑，只关心当前根节点的前驱节点即可
                head = root
            else:
                pre.right = root
                root.left = pre
            pre = root  # 当前节点变成前驱节点

            inorder(root.right)

        if not root:
            return None

        pre, head = None, None
        inorder(root)

        # 构建循环链表
        head.left = pre
        pre.right = head

        return head

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """中序遍历存储节点，然后更改指针"""
        def inorder(root: Node):
            nonlocal path
            if not root:
                return None
            
            inorder(root.left)
            path.append(root)
            inorder(root.right)

        path = []
        inorder(root)

        if len(path) == 0:
            return None

        for i in range(len(path)):
            path[i].right = path[(i+1) % len(path)]
            path[i].left = path[(i-1+len(path)) % len(path)]
        
        return path[0]