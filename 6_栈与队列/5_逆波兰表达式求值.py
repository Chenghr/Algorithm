"""
    题目描述:
        根据 逆波兰表示法，求表达式的值。
        有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

    说明:
        整数除法只保留整数部分。
        给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

    提示:
        1 <= tokens.length <= 104
        tokens[i] 要么是一个算符（"+"、"-"、"*" 或 "/"），要么是一个在范围 [-200, 200] 内的整数

    链接: https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
"""

class Solution:
    def _cal(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            # 整数除法只保留整数部分
            return int(num1 / num2)
        else:
            raise ValueError('op is invalid.')
    
    def evalRPN(self, tokens: list[str]) -> int:
        nums_stack = []
        op = ['+', '-', '*', '/']

        for str in tokens:
            if str in op:
                # 运算符
                num2 = nums_stack.pop()
                num1 = nums_stack.pop()
                # 注意这里操作数和被操作数的顺序问题
                result = self._cal(num1, num2, str)

                nums_stack.append(result)
            else:
                # 数字
                nums_stack.append(int(str))
        
        return nums_stack[0]

    def evalRPN_prior(self, tokens: list[str]) -> int:
        """写的复杂了，考虑了运算符的优先级
        """
        op_stack, nums_stack = [], []
        op_prior = {
            '+': 1, 
            '-': 1, 
            '*': 2, 
            '/': 2
        }

        for str in tokens:
            if str in op_prior:
                # 运算符
                if len(op_stack) == 0 or op_prior[str] > op_prior[op_stack[-1]]:
                    op_stack.append(str)
                else:
                    op = op_stack.pop()
                    num2 = nums_stack.pop()
                    num1 = nums_stack.pop()
                    # 注意这里操作数和被操作数的顺序问题
                    result = self._cal(num1, num2, op)

                    nums_stack.append(result)
                    op_stack.append(str)
            else:
                # 数字
                nums_stack.append(int(str))
        
        while len(op_stack) != 0:
            op = op_stack.pop()
            num2 = nums_stack.pop()
            num1 = nums_stack.pop()
            # 注意这里操作数和被操作数的顺序问题
            result = self._cal(num1, num2, op)

            nums_stack.append(result)
        
        return nums_stack[0]


if __name__ == '__main__':
    solution = Solution()
    tokens = ["2","1","+","3","*"]

    result = solution.evalRPN(tokens)
    print(result)