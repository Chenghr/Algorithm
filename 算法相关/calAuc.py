from sklearn.metrics import roc_curve, auc 
import numpy as np 
from collections import defaultdict

label = [1, 1, 0, 0, 1, 1, 0]
pred = [0.8, 0.7, 0.5, 0.5, 0.5, 0.5, 0.3]

# label = [0, 0, 1, 1]
# pred = [0.1, 0.4, 0.35, 0.8]

def calAuc1(prob,labels):
    """不含重复 prob 的计算"""
    f = list(zip(prob,labels))
    rank = [label for _, label in sorted(f,key=lambda x:x[0])]
    rankList = [i+1 for i in range(len(rank)) if rank[i]==1]

    posNum = sum(labels)
    negNum = len(labels) - posNum

    auc = (sum(rankList)- (posNum*(posNum+1))/2)/(posNum*negNum)
    return auc

def calAuc(probs, labels):
    """含有重复 prob 的计算"""
    f = list(zip(probs, labels))
    f.sort(key = lambda x: x[0])

    dic = defaultdict(int)
    rank = []  
    for i, (prob, _) in enumerate(f):
        # 遍历升序序列，获得初始 rank 值以及统计 prob 出现的次数
        dic[prob] += 1
        rank.append(i+1)
    
    i = 0
    while i < len(labels):
        prob = f[i][0]

        if dic[prob] > 1:
            # 利用等差数列的性质，计算均值，修正 rank 值
            rank[i: i+dic[prob]] = [rank[i] + (dic[prob]-1)/2] * dic[prob]
            i += dic[prob]
        else:
            i += 1
            
    # 获得所有正样本的 rank 值
    rankPos = [rank[i] for i in range(len(f)) if f[i][1] == 1]
    
    posNum = sum(labels)
    negNum = len(labels) - posNum

    auc = (sum(rankPos)- (posNum*(posNum+1))/2)/(posNum*negNum)
    return auc

def calAuc_v1(probs, labels):
    """含有重复 prob 的计算"""
    f = list(zip(probs, labels))
    f.sort(key=lambda x: x[0])

    ranks = [i+1 for i in range(len(labels))]  # 获取所有排序后样本的 rank

    # 更新相同概率的样本对应的rank
    i = 0
    while i < len(labels):
        j = i + 1
        while j < len(labels) and f[j][0] == f[i][0]:
            j += 1

        if j > i+1:
            # 说明出现相同概率的样本，区域为[i, j)
            # i 对应 rank 为 i+1, j-1对应rank 为 j，公差为1，取均值
            ranks[i: j] = [(i+j+1)/2] * (j-i)

        i = j

    # 获取更新后的正例样本 rank
    ranksPos = [ranks[i] for i in range(len(labels)) if f[i][1] == 1]

    posNum = sum(labels)
    negNum = len(labels) - posNum

    auc = (sum(ranksPos)- (posNum*(posNum+1))/2)/(posNum*negNum)
    return auc

ans = calAuc_v1(pred, label)
# pred = pred.sort()
# ans = auc(np.array(pred), np.array(label))
print(ans)