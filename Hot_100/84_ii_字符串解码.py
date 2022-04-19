"""
    题目描述:
        给定一个经过编码的字符串，返回它解码后的字符串。

        编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。
        注意 k 保证为正整数。

        你可以认为输入字符串总是有效的；
        输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

        此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

    链接: https://leetcode-cn.com/problems/decode-string
"""

class Solution:
    def decodeString(self, s: str) -> str:
        """
            1. 注意数字可能是多位数；
            2. 仅针对[]内的数字重复, 即注意 [] 的内部嵌套

            1. 使用栈来模拟操作，将连续数字、连续字符、括号作为一个单元存储；
            2. 具体的:
                    连续数字、连续字符、左括号均入栈；
                    右括号则出栈直到遇到左括号，将出栈拼接的字符转逆序；
                    栈顶数字出栈，乘以字符串，再入栈；
                最终栈顶元素为最终结果
        """
        stack = []
        
        i = 0
        while i < len(s):
            if s[i] == '[':
                stack.append(s[i])
                i += 1
            elif s[i].isalpha():
                # 找连续字符
                j = i + 1
                while j < len(s) and s[j].isalpha():
                    j += 1
                stack.append(s[i: j])
                i = j
            elif s[i].isalnum():
                # 找连续数字 
                j = i + 1
                while j < len(s) and s[j].isalnum():
                    j += 1
                stack.append(int(s[i: j]))
                i = j
            elif s[i] == ']':
                encodeStr = ''

                while stack[-1] != '[':
                    str1 = stack.pop()  # 规则
                    encodeStr = str1 + encodeStr

                _ = stack.pop()  # 出 '['
                repeatNum = stack.pop()
                decodeStr = encodeStr * repeatNum
                stack.append(decodeStr)
                i += 1
        
        ans = "".join(stack)
        return ans

    def decodeString(self, s: str) -> str:
        """
            递归处理；
            从左向右解析；
            
            当 s[i] == ']' 时，返回当前括号内记录的 res 字符串与 ] 的索引 i （更新上层递归指针位置）；
            当 s[i] == '[' 时，开启新一层递归，记录此 [...] 内字符串 tmp 和递归后的最新索引 i，
            并执行 res + multi * tmp 拼接字符串。
            遍历完毕后返回 res。
        """
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)

a = Solution()
ans = a.decodeString("3[a]2[bc]")
print(ans)