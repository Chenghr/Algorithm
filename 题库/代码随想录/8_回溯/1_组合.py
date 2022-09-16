"""
    题目描述:
        给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
    
    提示:
        1 <= n <= 20
        1 <= k <= n
    
    链接: https://leetcode-cn.com/problems/combinations/
"""

"""
    回溯算法基本框架:

    def backtracking(参数): 

        if (终止条件) :
            存放结果;
            return;

        for (选择: 本层集合中元素（树中节点孩子的数量就是集合的大小）) 
            处理节点;
            backtracking(路径，选择列表); // 递归
            回溯，撤销处理结果
"""

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combine_list = []

        def _backtracking(begin:int, end:int, result: List[int], k):
            if len(result) == k:
                nonlocal combine_list
                combine_list.append(result.copy())
            
            for num in range(begin, end):
                result.append(num)
                _backtracking(num+1, end, result, k)
                result.pop()
        
        _backtracking(1, n+1, [], k)

        return combine_list

    def combine(self, n: int, k: int) -> List[List[int]]:
        """剪枝版本
        """

        result, path = [], []

        def _backtracking(n, k, begin):

            nonlocal result, path

            if len(path) == k:
                result.append(path.copy())
                return
            
            for num in range(begin, n - (k-len(path)) + 2):
                path.append(num)
                _backtracking(n, k, num+1)
                path.pop()
        
        _backtracking(n, k, 1)

        return result