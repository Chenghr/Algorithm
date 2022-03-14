"""
    题目描述: 
        这里有 n 个航班，它们分别从 1 到 n 进行编号。

        有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 
        意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

        请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。

    链接: https://leetcode-cn.com/problems/corporate-flight-bookings
"""

from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
            标准的差分数组题，没什么好说的。
            注意航班编号从 1 开始的。
        """
        # 差分数组初始为0，每个航班都没订座位
        diff = [0] * (n+1)

        for booking in bookings:
            diff[booking[0]] += booking[2]

            if booking[1]+1 < n+1:
                diff[booking[1]+1] -= booking[2]
        
        seats = [diff[0]] * (n+1)

        for i in range(1, n+1):
            seats[i] = seats[i-1] + diff[i]
        
        return seats[1:]
            