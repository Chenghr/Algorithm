"""
    请实现两个函数，分别用来序列化和反序列化二叉树。

    你需要设计一个算法来实现二叉树的序列化与反序列化。
    这里不限定你的序列 / 反序列化算法执行逻辑，
    你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。 
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root: TreeNode):
        """递归，先根遍历
        """
        if not root:
            return "#,"
        
        res = str(root.val) + ','
        res += self.serialize(root.left)
        res += self.serialize(root.right)

        return res

    def deserialize(self, data: str):
        """递归处理节点;
            注意这里的 iter 的巧妙用法
            或者使用 deque 的 popleft 或者 list 的 pop(0) 也是可以的，效果相同.
        """
        data = iter(data.split(','))

        def helper() -> TreeNode:
            nonlocal data

            val = next(data)
            if val == '#':
                return None
            
            root = TreeNode(int(val))
            root.left = helper()
            root.right = helper()

            return root
        
        return helper()


class Codec:

    def serialize(self, root):
        """层次遍历，相邻节点之间使用 ',' 隔开，'#' 表示空节点
        """
        if not root:
            return ""

        que = deque()
        que.append(root)

        ans = ""
        while que:
            node = que.popleft()

            if not node:  # 空节点
                ans += "#,"
                continue

            ans += str(root.val) + ',' # 避免val为多位数，str后有多个字符数字

            que.append(root.left)
            que.append(root.right)        
        
        return ans

    def deserialize(self, data: str):
        """
            注意这里的 iter 的巧妙用法
        """
        if not data:
            return None
        
        data = iter(data.split(','))
        root = TreeNode(next(data))

        que = deque()
        que.append(root)
        
        while que:
            node = que.popleft()
            left, right = next(data), next(data)

            if left != '#':
                node.left = TreeNode(int(left))
                que.append(node.left)
            if right != '#':
                node.right = TreeNode(int(right))
                que.append(node.right)
        
        return root