"""
    题目描述:
        有 n 类物品和一个最多能背重量为 w 的背包。
        第 i 类物品的重量是 weight[i]，得到的价值是 value[i] 。
        每类物品有无限件，求解将哪些物品装入背包里物品价值总和最大。

    完全背包和01背包问题唯一不同的地方就是，每种物品有无限件。
    完全背包问题的难点在于遍历顺序上。
"""

def complete_pack(bag_size, weight, value):
    """
        1. 转化为 01 背包求解:
            对于容量 c 的背包，每类物品的最大选择个数为 c/w[i]；
            因此可以将完全背包转化为物品数更多的 01 背包问题进行求解。
        
        2. 进一步的，基于二进制思想可以改进:
            把第i种物品拆成费用为 C_i * 2^k、价值为 W_i * 2^k 的若干件物品，
            其中 k 取遍满足 C_i * 2^k ≤ V 的非负整数。

            这是二进制的思想。 
            因为不管最优策略选几件第i种物品, 其件数写成二进制后，总可以表示成若干个 2^k 件物品的和。
    """
    """
        采用二维递推;

        1. dp[i][j]:
            容量为 j 的背包在前 i 类物品中获得的最大价值;

        2. 递推公式:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k*w[i]] + k*v[i]);
            其中 0 <= k*w[i] <= j;

        3. 初始化（与定义要吻合）: 
            dp[i][0]: 
                背包容量为 0 ，最大价值一定为 0；

            dp[0][j]:
                背包容量小于 w[0] 时，装不下，最大价值为 0；
                背包容量大于等于 w[0] 时，最大价值为 v[0]*[j/w[0]] (向下取整);

        4. 遍历顺序:
            先物品后背包容量，顺序遍历即可。
    """
    dp = [[0] * (bag_size+1) for _ in range(len(weight))]

    # 初始化
    for j in range(bag_size+1):
        if j >= weight[0]:
            dp[0][j] = value[j] * int(j / weight[0])
    
    # 遍历
    for i in range(len(weight)):
        for j in range(bag_size+1):
            for k in range(int(j / weight[i])):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-k*weight[i]] + k*value[i])
    
    return dp[-1][-1]
    

def complete_pack(bag_size, weight, value):
    """
        与01背包类似，完全背包也可以用滚动数组来进行空间压缩；
        与之前不同的是，完全背包场景下滚动数组会带来更小的时间开销。

        由于每一类物品有无限个，因此在背包容量遍历时，需要顺序遍历，而非倒序遍历。
    """
    dp = [0 for _ in range(bag_size+1)]

    # 假设价值非负，因此初始化均为0即可

    for i in range(len(weight)):
        for j in range(bag_size+1):
            # 保证数组的下标非负
            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])

    return dp[bag_size]
