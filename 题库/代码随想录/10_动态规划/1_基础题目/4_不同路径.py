"""
    题目描述:
        一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
        机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
        问总共有多少条不同的路径？

    链接: https://leetcode-cn.com/problems/unique-paths
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
            1. dp[i][j]，二维数组，到达(i, j)的路径数目;
            2. 递推公式:
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            3. 初始化:
                dp[0][i] = 1; dp[j][0] = 1;
            4. 遍历顺序:
                逐行遍历，除去边界 
        """
        dp = [[0] * n] * m

        # 初始化
        for i in range(0, n):
            dp[0][i] = 1
        
        for i in range(0, m):
            dp[i][0] = 1
        
        # 递推
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

"""
    本题的其他解法:
    
    1. 深搜
        机器人走过的路径可以抽象为一棵二叉树，而叶子节点就是终点；
        问题就可以转化为求二叉树叶子节点的个数。
    
    2. 动态规划:
        进阶考虑状态压缩，使用滚动数组压缩空间；
    
    3. 数论方法:
        转化为组合问题；
        求组合的时候，要防止两个int相乘溢出;
"""