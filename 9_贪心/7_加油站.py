"""
    题目描述:
        在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
        你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
        你从其中的一个加油站出发，开始时油箱为空。

        给定两个整数数组 gas 和 cost ，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。
        如果存在解，则 保证 它是 唯一 的。

    链接: https://leetcode-cn.com/problems/gas-station
"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            暴力求解，模拟跑圈，O(n*2)
        """
        for start_idx in range(len(gas)):

            rest = gas[start_idx] - cost[start_idx]
            idx = (start_idx + 1) % len(gas)

            while rest >= 0 and idx != start_idx:
                # 模拟行驶一圈
                rest += gas[idx] - cost[idx]
                idx = (idx+1) % len(gas)

            if rest >= 0 and idx == start_idx:
                return start_idx
        
        return -1
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            贪心:
                局部最优:
                    当前累加rest[j]的和curSum一旦小于0，起始位置至少要是j+1，
                    因为从j开始一定不行。
                    j之前出现了多少负数，j后面就会出现多少正数，因为耗油总和是大于零的
                全局最优: 
                    找到可以跑一圈的起始位置。
        """
        if sum(gas) < sum(cost):
            return -1

        curSum, start_idx = 0, 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]

            if curSum < 0:
                start_idx = i+1
                curSum = 0
        
        return start_idx


    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            全局考虑，巧妙的思路
        """
        curSum = 0
        minGas = float('inf')  # 从起点出发，邮箱所需最小汽油数

        for i in range(len(gas)):
            curSum += gas[i] - cost[i]

            minGas = min(minGas, curSum)
        
        if curSum < 0:
            # 所有的汽油不够总消耗
            return -1
        
        if minGas >= 0:
            # 从起点出发可以达到终点
            return 0
        
        # 从后向前遍历，看什么时候能把从起点的所需汽油数补齐
        for i in range(len(gas)-1, 0, -1):
            minGas += gas[i] - cost[i]

            if minGas >= 0:
                return i
        
        return -1
    


example = Solution()
result = example.canCompleteCircuit([2,3,4],[3,4,3])
print(result)


