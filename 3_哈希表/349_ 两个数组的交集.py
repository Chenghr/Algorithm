"""
给定两个数组，编写一个函数来计算它们的交集。

说明：
    输出结果中的每个元素一定是唯一的。
    我们可以不考虑输出结果的顺序。

https://leetcode-cn.com/problems/intersection-of-two-arrays/
"""

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        from collections import defaultdict

        num_dict = defaultdict(int)

        for num in nums1:
            # 仅标记是否出现
            num_dict[num] = 1
        
        result = []

        for num in nums2:
            if num_dict[num] > 0:
                result.append(num)
                # 保证输出结果中的元素唯一
                num_dict[num] -= 1
        
        return result

        # 两个数组先变成集合，求交集后还原为数组
        # return list(set(nums1) & set(nums2)) 

# 相关知识:
"""collections.defaultdict类的介绍：

使用普通的字典时，用法一般是dict={},添加元素的只需要dict[element] =value，
调用的时候也是如此，dict[element] = xxx,但前提是element字典里，如果不在字典里就会报错；

defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值

dict = defaultdict(factory_function)

    factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值；
    比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0；
"""

"""python set函数

set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
"""