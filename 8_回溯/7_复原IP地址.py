"""
    题目描述:
        有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），
        整数之间用 '.' 分隔。

    例如: "0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，
    但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
    
    给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，
    返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。
    你不能重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
    
    提示:
        0 <= s.length <= 20
        s 仅由数字组成
    
    链接: https://leetcode-cn.com/problems/restore-ip-addresses
"""

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
            类似上一题的分割回文串，每次插入'.'时检测分割数字是否符合标准；
            具体的分成两个问题:
                判断截取数字是否合规 + 回溯
        """

        result, path = [], []

        def _backtracking(s: str, begin_idx: int) -> None:
            nonlocal result, path
            
            # 递归终点
            if begin_idx >= len(s):
                if len(path) == 4:
                    ip = path[0]

                    for i in range(1, len(path)):
                        ip = ip + '.' + path[i]

                    result.append(ip)

                return
            
            # 单层逻辑
            for end_idx in range(begin_idx+1, len(s)+1):
                # 左闭右开
                if len(path) == 3 and end_idx != len(s):
                    continue

                if self.isOk(s[begin_idx: end_idx]):

                    path.append(s[begin_idx: end_idx])
                    
                    _backtracking(s, end_idx)

                    path.pop()

        if len(s) < 4:
            return []

        _backtracking(s, 0)
        
        return result

    def isOk(self, s: str) -> bool:
        """
            合法的数有两个限制:
                1. 前导0限制
                2. 数的大小限制
        """
        if len(s) > 1 and s[0] == '0':
            # 整数不能含有前导0
            return False
        
        num = int(s)

        if num < 0 or num > 255:
            # 数的大小限制
            return False
        
        return True
