"""
    题目描述:
        有 N 种物品和一个容量为 V 的背包。
        第 i 种物品最多有 Mi 件可用，每件耗费的空间是 Ci ，价值是 Wi 。
        求解将哪些物品装入背包可使这些物品的耗费的空间 总和不超过背包容量，且价值总和最大。
"""

"""
    求解思路:
    1. 转化为 01 背包求解:
        每件物品最多有 Mi 件可用，把 Mi件摊开，其实就是一个 01 背包问题了；
        或者把每种商品遍历的个数放在01背包里面在遍历一遍。
    
    2. 基于二进制的优化: 
        将第i种物品分成若干件01背包中的物品， 
        其中每件物品有一个系数。这件物品的费用和价值均是原来的费用和价值乘以这个系数。
        令这些系数 分别为1, 2, 2^2, ..., 2^(k-1), Mi - 2^k + 1, 
        其中 k 是满足 Mi - 2^k + 1 > 0的最大整数。

        时间复杂度: O(V * ΣMi) -> O(V * ΣlogMi)
"""

def test_multi_pack1():
    """ 转化为 01 背包求解
    """
    weight = [1, 3, 4]
    value = [15, 20, 30]
    nums = [2, 3, 2]
    bag_weight = 10

    for i in range(len(nums)):
        # 将物品展开数量为1
        while nums[i] > 1:
            weight.append(weight[i])
            value.append(value[i])
            nums[i] -= 1
    
    dp = [0]*(bag_weight + 1)

    # 遍历物品
    for i in range(len(weight)):
        # 遍历背包
        for j in range(bag_weight, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    
    print(" ".join(map(str, dp)))

def test_multi_pack2():
    """增加遍历次数
    """
    weight = [1, 3, 4]
    value = [15, 20, 30]
    nums = [2, 3, 2]
    bag_weight = 10

    dp = [0]*(bag_weight + 1)

    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            # 以上是01背包，加上遍历个数
            for k in range(1, nums[i] + 1):
                if j - k*weight[i] >= 0:
                    dp[j] = max(dp[j], dp[j - k*weight[i]] + k*value[i])

    print(" ".join(map(str, dp)))
