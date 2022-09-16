from collections import defaultdict

class Node:
    def __init__(self, k) -> None:
        self.acc = [0, k]

        dic = defaultdict(int)
        dic[k] = 0
        self.deny = dic

nums = list(map(int, input().split()))
n, m ,k = nums[0], nums[1], nums[2]

locs = list(map(int, input().split()))
gain_stable = list(map(int, input().split()))
gain_change = list(map(int, input().split()))

dic = defaultdict(int)
node_pre = [[0, k], dic]

for i in range(m):
    dic_new = defaultdict(int)
    node_new = node_pre[:]

    # 接受
    max_gain = 0
    if node_pre[0][1] == locs[i]:
        max_gain = max(max_gain, node_pre[0][0] + gain_stable[i])
    else:
        max_gain = max(max_gain, node_pre[0][0] + gain_change[i])

    for key in node_pre[1].keys():
        if key == locs[i]:
            max_gain = max(max_gain, node_pre[1][key] + gain_stable[i])
        else:
            max_gain = max(max_gain, node_pre[1][key] + gain_change[i])
    
    node_new[0] = [max_gain, locs[i]]

    # 不接受
    node_new[1] = node_pre[1]
    node_new[1][node_pre[0][1]] = max(node_new[1][node_pre[0][1]], node_pre[0][0])
    
    node_pre = node_new

print(node_pre[0][0])

