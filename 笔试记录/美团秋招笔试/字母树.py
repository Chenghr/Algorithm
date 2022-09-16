from collections import defaultdict

class TreeNode:
    def __init__(self, tag: int, val: str):
        self.tag = tag
        self.val = val
        self.childs = []

def sumCh(root, n):
    res = [0 for _ in range(n)]

    def postOrder(root: TreeNode):
        nonlocal res
        
        if not root:
            return set()

        ans = set([root.val])
        for child in root.childs:
            temp = postOrder(child)
            ans = ans | temp
    
        res[root.tag] = len(ans)

        return ans
    
    _ = postOrder(root)

    return res

n = int(input())
line = input().strip()
fathers = list(map(int, line.split()))
vals = input().strip()

nodes = []
for i in range(n):
    nodes.append(TreeNode(i, vals[i]))

for i in range(1, n):
    nodes[fathers[i-1]-1].childs.append(nodes[i])

if n == 0:
    ans = []
else:
    ans = sumCh(nodes[0], n)

for num in ans:
    print(num)
