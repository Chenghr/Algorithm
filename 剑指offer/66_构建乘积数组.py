"""
    给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
    其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 
    即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
"""

from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        """
            优化空间
            由于输出数组不算在空间复杂度内，那么我们可以将 L 或 R 数组用输出数组来计算。
            先把输出数组当作 L 数组来计算，然后再动态构造 R 数组得到结果。
        """
        length = len(a)
        answer = [0]*length
        
        # answer[i] 表示索引 i 左侧所有元素的乘积
        # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1
        answer[0] = 1
        for i in range(1, length):
            answer[i] = a[i - 1] * answer[i - 1]
        
        # R 为右侧所有元素的乘积
        # 刚开始右边没有元素，所以 R = 1
        R = 1;
        for i in reversed(range(length)):
            # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
            answer[i] = answer[i] * R
            # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
            R *= a[i]
        
        return answer

    def constructArr(self, a: List[int]) -> List[int]:
        """
            构造前缀积和后缀积，对应相乘即可
        """
        if len(a) == 0:
            return []

        pre = [1] * len(a)
        ans = [1] * len(a)

        for i in range(1, len(a)):
            pre[i] = pre[i-1] * a[i-1]
            ans[len(a)-1-i] = ans[len(a)-i] * a[len(a)-i]
        
        ans = [pre[i]*ans[i] for i in range(len(a))]

        return ans

