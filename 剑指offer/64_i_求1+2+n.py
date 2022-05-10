"""
    求 1+2+...+n ，
    要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""

class Solution:
    def sumNums(self, n: int) -> int:
        """
            解题思路:
                1. 平均计算
                    需要使用乘除法，不可取
                2. 迭代
                    需要使用 while 或者 for，不可取
                3. 递归
                    终止条件需要 if，不可取

                    考虑使用其他的方法终结递归
                    常见的逻辑运算符有三种，即 “与 & ”，“或 | ”，“非 !” ；而其有重要的短路效应，
                    if A & B:
                        若 A 为 false，则 B 的判断不会执行，即短路；
                    
                    if A | B:
                        若 A 为 true ，则 B 的判断不会执行（即短路）
                    
                    本题需要实现 “当 n = 1 时终止递归” 的需求，可通过短路效应实现
        """
        ans = 0

        def dfs(n: int):
            nonlocal ans

            n > 1 and dfs(n-1)
            ans += n
        
        dfs(n)
        return ans