"""
    请实现一个函数，用来判断一棵二叉树是不是对称的。
    如果一棵二叉树和它的镜像一样，那么它是对称的。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
            递归求解；
            判断左右子树是否互为镜像，重点在于两棵树的指针移动是反向的
        """
        def compare(root1: TreeNode, root2: TreeNode):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2 or root1.val != root2.val:
                # 左右子树有一个为空，或者左右子树值不同，不为镜像
                return False
            
            # 现在左右子树均不为空了，且左右子树值相同
            # 递归的判断左右子树是否为镜像
            outSide = compare(root1.left, root2.right)
            inSide = compare(root1.right, root2.left)

            return inSide and outSide
        
        if not root:
            return True

        # 判断左右子树是否互为镜像
        return compare(root.left, root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        """
            迭代求解；
            本题的核心点在于左右子树是否互为镜像的判断，进一步在于遍历指针的顺序问题；
            迭代方法知识借助额外容器存储了节点而已。

            层次遍历
        """
        def compare(root1: TreeNode, root2: TreeNode):
            from collections import deque

            que1, que2 = deque(), deque()
            que1.append(root1)
            que2.append(root2)

            while len(que1) != 0 and len(que2) != 0:
                node1 = que1.popleft()
                node2 = que2.popleft()

                if not node1 and not node2:
                    continue

                if not node1 or not node2 or node1.val != node2.val:
                    # 左右子树有一个为空，或者左右子树值不同，不为镜像
                    return False
                
                # 到这里说明两个节点均不为空，且值相同
                que1.append(node1.left)  
                que1.append(node1.right)
                
                que2.append(node2.right)  # 注意这里的入队顺序
                que2.append(node2.left)
            
            return len(que1) == len(que2)  # 可能有一个遍历完但是另一个没有的情况
        
        if not root:
            return True

        # 判断左右子树是否互为镜像
        return compare(root.left, root.right)
    
    """
        迭代法可以进一步优化，只用一个队列即可；
        初始:  
            que.append(root.left)  
            que.append(root.right)
        中间:
            que.append(node1.left)  
            que.append(node2.right)
            que.append(node1.right)
            que.append(node2.left)
            
        每次取队首的两个节点比较即可。
    """

            
            
            
