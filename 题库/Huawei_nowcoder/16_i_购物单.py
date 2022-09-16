"""
    链接: https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4?tpId=37&tqId=21239&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D3%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=3&judgeStatus=undefined&tags=&title=
"""
import sys 
from collections import defaultdict

if __name__ == "__main__":
    """
        01 背包问题
        每个主件最多有2个不同附件；那么最终的选项最多有4个:
            1. 仅买主件；2. 买主件+附件1；3. 买主件+附件2；4.买主件+两个附件

    """
    # 读取第一行的n
    money, itemsNum = map(int, sys.stdin.readline().split())
    money //= 10  # 价格均为 10 的倍数，优化空间复杂度

    prices = defaultdict(lambda: [0, 0, 0])  # 主从物品的价格
    values = defaultdict(lambda: [0, 0, 0])  # 主从物品的价值

    # i 代表第 i + 1 个物品
    for i in range(itemsNum):
        v, p, q = map(int, sys.stdin.readline().split())
        v //= 10            # 价格总为 10 的倍数，优化空间复杂度

        if q == 0:          # 追加主物品
            prices[i + 1][0] = v
            values[i + 1][0] = v * p
        elif prices[q][1]:  # 第一次追加从物品
            prices[q][2] = v
            values[q][2] = v * p
        else:               # 追加第二个从物品
            prices[q][1] = v
            values[q][1] = v * p
    
    # 处理输出
    dp = [0] * (money + 1)  # 初始化 dp 数组
    
    for i, v in prices.items():
        for j in range(money, v[0] - 1, -1):
            p1, p2, p3 = v
            v1, v2, v3 = values[i]
            # 处理主从组合的四种情况
            dp[j] = max(dp[j], dp[j - p1] + v1)  # 仅选择主物品
            dp[j] = max(dp[j], dp[j - p1 - p2] + v1 + v2) if j >= p1 + p2 else dp[j]  # 主+附1
            dp[j] = max(dp[j], dp[j - p1 - p3] + v1 + v3) if j >= p1 + p3 else dp[j]  # 主+附2
            dp[j] = max(dp[j], dp[j - p1 - p2 - p3] + v1 + v2 + v3) if j >= p1 + p2 + p3 else dp[j]  # 主+所有附件
    
    print(dp[money] * 10)

        
        