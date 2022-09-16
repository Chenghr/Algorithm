"""
    题目描述:
        给你一个整数 n ，
        求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？
        返回满足题意的二叉搜索树的种数。
    
    链接: https://leetcode-cn.com/problems/unique-binary-search-trees/
"""

class Solution:
    def numTrees(self, n: int) -> int:
        """
            本题的难点在于递推公式的构造；
            分析时抓住一点，dp[i] 不仅表示节点值从 1 到 i 互不相同的二叉搜索树数目；
            更表示连续升序长为 i 的二叉搜索树数目；

            dp[i] 可以分别由 i 个值构成根节点，然后左右子树总节点和为 i-1;
            由此可知:

            1. dp[i]: 节点值从 1 到 i 互不相同的二叉搜索树数目；
            2. dp[i] = sum(dp[j] * dp[i-1-j]), j in [0, i-1] (左右子树可以为空);
            3. 初始化:
                dp[0] = 1, dp[1] = 1;
            4. 从前向后遍历
        """
        dp = [1] * (n+1)

        for i in range(2, n+1):
            
            dp[i] = 0

            for j in range(0, i):
                dp[i] += dp[j] * dp[i-1-j]
        
        return dp[n]