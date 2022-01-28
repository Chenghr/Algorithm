"""
    题目描述:
        给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi] 表示飞机出发和降落的机场地点。
        请你对该行程进行重新规划排序。

        所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。
        如果存在多种有效的行程，请你按字典排序返回最小的行程组合。

        例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。
        假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。

    提示:
        1 <= tickets.length <= 300
        tickets[i].length == 2
        fromi.length == 3
        toi.length == 3
        fromi 和 toi 由大写英文字母组成
        fromi != toi

    链接: https://leetcode-cn.com/problems/reconstruct-itinerary
"""

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
            思路:
                图论中的深搜算法；
            
            几个难点:
                1. 死循环的问题如何解决？
                2. 字母序排列问题，如何记录映射关系？
                3. 深搜中的终止条件是什么？
                4. 如何遍历一个机场所对应的所有机场？
        """
        

        # 将票处理成字典，方便遍历
        tickets_dict = defaultdict(list)

        for ticket in tickets:
            tickets_dict[ticket[0]].append(ticket[1])

        path = ['JFK']  # 固定起点

        def _backtracking(start_point):
            nonlocal path

            if len(path) == len(tickets)+1:
                # 深搜的终止条件，找到一条完整路径
                return True

            # 到达机场按照字典序排序，解决字典序问题
            tickets_dict[start_point].sort()  

            for _ in tickets_dict[start_point]:
                
                # 将去过的 ticiket 删除掉，避免死循环
                end_point = tickets_dict[start_point].pop(0)
                path.append(end_point)

                # 递归，找到一个可行解就结束
                if _backtracking(end_point):
                    return True
                
                # 回溯，将删除的节点加回去
                tickets_dict[start_point].append(end_point)
                path.pop()


        _backtracking('JFK')

        return path
                
                    
