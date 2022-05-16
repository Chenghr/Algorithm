"""https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
            先根遍历；
            相邻节点间字符用 ',' 隔开，空节点添加 '#'
        """
        ans = ''

        def preOrder(root: TreeNode):
            nonlocal ans

            if not root:
                ans += '#,'
                return
            
            ans += str(root.val) + ','

            preOrder(root.left)
            preOrder(root.right)
            
        preOrder(root)

        return ans

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

            先根遍历
        """
        data, index = data.split(','), 0

        def preOrderConstruct() -> TreeNode:
            nonlocal data, index

            if index == len(data):
                return None
            
            if data[index] == '#':
                index += 1
                return None
                
            node = TreeNode(int(data[index]))
            index += 1

            node.left = preOrderConstruct()
            node.right = preOrderConstruct()

            return node
        
        return preOrderConstruct()