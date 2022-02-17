"""
    题目描述:
        有 n 件物品和一个最多能背重量为 w 的背包。
        第 i 件物品的重量是 weight[i]，得到的价值是 value[i] 。
        每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
"""

def wei_bag_01_problem(bag_size, weight, value) -> int: 
    """
        暴力搜索，回溯法
    """


def wei_bag_01_problem(bag_size, weight, value) -> int: 
    """
        动态规划:
        1. dp[i][j]: 容量为 j 的背包在前 i 个物品中取，装入背包的物品价值总和最大值；

        2. 对于第 i 个物品，有取和不取两种选择，取其中较大的那个:
            dp[i][j] = max( dp[i-1][j], dp[i-1][j-w[i]] + v[i] )
        
        3. 初始化（与定义要吻合）: 
            dp[i][0]: 
                背包容量为 0 ，最大价值一定为 0；

            dp[0][j]:
                背包容量小于 w[0] 时，装不下，最大价值为 0；
                背包容量大于等于 w[0] 时，最大价值为 v[0];
        
        4. 遍历顺序:
            先遍历物品，即 i；再遍历背包容量 j.
    """
    dp = [[0] * (bag_size+1)] * len(weight)

    # 初始化
    for j in range(bag_size+1):
        if j >= weight[0]:
            dp[0][j] = value[j]
    
    # 遍历
    for i in range(len(weight)):
        for j in range(bag_size+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
    
    return dp[-1][-1]


def wei_bag_01_problem(bag_size, weight, value) -> int: 
    """
        动态规划-滚动数组:
        上一个解法中， dp[i][j]仅与 dp[i-1] 以及 dp[i][j] 之前的值有关；
        如果把dp[i - 1]那一层拷贝到dp[i]上，可以将推导公式改写为:
            dp[i][j] = max( dp[i][j], dp[i][j-w[i]] + v[i] );
        进一步的，可以只用一个一维数组:
            dp[j] = max( dp[j], dp[j-w[i]] + v[i] )
        注意此时要从后向前遍历，否则会用新值覆盖掉旧值，干扰后续的更新；

        完整的动态规划分析如下:
        1. dp[j]: 容量为j的背包，所背的物品价值可以最大为dp[j]。
        2. 递推公式:
            dp[j] = max( dp[j], dp[j-w[i]] + v[i] )
        3. 初始化:
            根据定义: dp[0] = 0;
            对于非 0 下标，看一下递推公式，取得是最大值，因此只要初始化的比价值序列中的最小值还小即可；
            对于非负 v[i], 初始化为 0 即可。（避免被初始值覆盖）
        4. 遍历顺序:
            先遍历物品，顺序遍历；再遍历背包容量，倒序遍历；

            - 倒序遍历背包容量为了保证物品只被放入背包一次；也就是上面提到的新值覆盖旧值（多次放入）的问题；
            - 必须先遍历物品:
                如果遍历背包容量放在上一层，那么每个dp[j]就只会放入一个物品，即: 背包里只放入了一个物品。

        滚动数组的使用条件:
            二维数组的上一层可以重复利用，直接拷贝到当前层。
    """
    dp = [0] * (bag_size+1)

    # 假设价值非负，因此初始化均为0即可

    for i in range(len(weight)):
        for j in range(bag_size+1, weight[i]-1, -1):
            # 保证数组的下标非负
            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])

    return dp[-1]