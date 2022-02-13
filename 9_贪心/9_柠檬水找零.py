"""
    题目描述:
        在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
        顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
        每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。
        你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

        注意，一开始你手头没有任何零钱。
        给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。
        如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

    链接: https://leetcode-cn.com/problems/lemonade-change
"""

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        own = {
            '5': 0,
            '10': 0,
            '20': 0
        }

        for bill in bills:
            own[str(bill)] += 1

            # 找零
            if bill == 20:
                if own['10'] > 0 and own['5'] > 0:
                    # 优先选择用 10 找零，因为 10 只能用于找零 20
                    own['10'] -= 1
                    own['5'] -= 1
                elif own['5'] >= 3:
                    own['5'] -= 3
                else:
                    return False

            elif bill == 10:
                if own['5'] > 0:
                    own['5'] -= 1
                else:
                    return False
        
        return True
            