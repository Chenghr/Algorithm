"""
    题目描述:
        给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

    注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

    提示:
        1 <= num1.length, num2.length <= 200
        num1 和 num2 只能由数字组成。
        num1 和 num2 都不包含任何前导零，除了数字0本身。

    链接: https://leetcode-cn.com/problems/multiply-strings
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
            模拟加法；
            注意处理好进位问题即可
        """
        ans = []  # 逆序存储结果，便于处理进位问题

        add = 0  # 进位
        i, j = len(num1)-1 ,len(num2)-1

        while i >= 0 or j >= 0 or add != 0:
            # 避免单独处理较长的数以及最高位进位问题
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0

            result = x + y + add

            ans.append(str(result % 10))
            add = result // 10

            i -= 1
            j -= 1
        
        return ''.join(ans[::-1])

    def multiply(self, num1: str, num2: str) -> str:
        """
            if num1 num2 之间有一个为0，则直接返回0
            均不为0，模拟竖式乘法，从右向左遍历乘数，将乘数每一位与被乘数相乘得到对应结果，再将结果累加。
            
            注意除了最低位外，其余每一位运算结果需要补0.
        """
        if num1 == '0' or num2 == '0':
            return '0'
        
        ans = '0'
        for i in range(len(num2)-1, -1, -1):
            y = int(num2[i])  # 当前乘数

            curr = ['0'] * (len(num2)-i-1)  # 结果；逆序存储；末位补0
            add = 0  # 进位

            for j in range(len(num1)-1, -1, -1):
                product = int(num1[j]) * y + add  # 当前乘积
                curr.append(str(product % 10))
                add = product // 10
            
            # 处理最高位的进位
            if add > 0:
                curr.append(str(add))
            
            curr = ''.join(curr[::-1])  # 逆序合并为最终结果

            ans = self.multiadd(ans, curr)  # 做字符串加法
        
        return ans

    def multiply(self, num1: str, num2: str) -> str:
        """
            在之前的基础上优化；使用数组代替字符串存储结果，减少对字符串的操作。

            num1 的长度为 m，num2 的长度为 n，则可以证明，乘积长度为 m+n-1 或 m+n;
            (分别去最小值和最大值验证)

            因此创建数组 ansArr 长为 m+n; num1[i] num2[j]的乘积结果存在 ansArr[i+j+1]；
            最后最高位如果是0则舍弃。
        """
        if num1 == '0' and num2 == '0':
            return '0'
        
        m, n = len(num1), len(num2)
        ansArr = [0] * (m+n)

        for i in range(m-1, -1, -1):
            x = int(num1[i])
            for j in range(n-1, -1, -1):
                ansArr[i+j+1] += x * int(num2[j])
            
            # 统一处理进位
            for i in range(m+n-1, 0, -1):
                ansArr[i-1] += ansArr[i] // 10
                ansArr[i] %= 10
            
        index = 1 if ansArr[0] == 0 else 0
        ans = ''.join(str(x) for x in ansArr[index:])

        return ans