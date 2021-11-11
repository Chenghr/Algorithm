"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

提示：
    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105

https://leetcode-cn.com/problems/3sum/
"""

"""
思路分析：
1. 暴力搜索
    使用三层 for 循环，直接筛选出所有结果。

2. 哈希法求解
    使用两层 for 循环确定 a+b，再用 hash 判断 -(a+b) 是否存在；
    但是这里有个问题就是三元组的去重问题不好解决；去重思路比较复杂，但是时间复杂度可以降低到 O(n^2)

3. 双指针法（最优）
    先用快速排序对数组进行排序，O(nlogn);
    再固定一个数，对另外两个数采用双指针法搜索，O(n^2); 整体时间复杂度 O(n^2)

    - 先考虑好顺序数组中的去重问题；
    - 再进一步的考虑优化，比如某些不可能的起始点；

# 去重思想
    先对数组进行排序，选择的三元组均从小到大排序，顺序选择三个数字，选择过程中考虑进去除重复数字。
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 双指针法
        if len(nums) < 3:
            return []

        # 或许需要自己写个快排回忆下
        nums.sort()  

        result = []

        for idx in range(len(nums)-2):

            # 效率优化，nums 为增序，如果第一个元素为整数，则不可能找到满足条件的三元组
            if nums[idx] > 0:
                break

            # 对第一个元素，进行去重
            if (idx >= 1 and nums[idx] == nums[idx-1]):
                continue

            left = idx + 1
            right = len(nums)-1

            while (left < right):
                if nums[idx] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[idx] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    # 记录当前解
                    result.append([nums[idx], nums[left], nums[right]])

                    # 寻找下个解前，注意排除掉相同元素
                    while (left < right and nums[left] == nums[left+1]):
                        left += 1
                    
                    while (left < right and nums[right] == nums[right-1]):
                        right -= 1
                    
                    # 注意这个不能丢掉
                    left += 1
                    right -= 1

        return result

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 哈希法求解
        # 没写出来，总感觉不对 ...... 看下面的链接吧
        # https://programmercarl.com/0015.三数之和.html#哈希解法
        pass

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))


# 额外知识
"""for 循环中迭代变量迭代问题:

初始代码去重中，写了如下的结构:

    for idx in range(len(nums)-2):
        ...
        ...
        while (idx < len(nums)-2 and nums[idx] == nums[idx+1]):
                    idx += 1

运行时出错，后续发现bug原因如下:

    在 python中，for 循环相当于一个迭代器（Iterator），在循环体中改变循环变量的值对循环次数是没有影响的。 

原因:
    迭代器在一个独立的线程中工作，并且拥有一个mutex锁。
    迭代器被创建的时候，建立了一个内存索引表（单链表），这个索引表指向原来的对象，当原来的对象数量改变的时候，这个索引表的内容没有同步改变，
    所以当索引指针往下移动的时候，便找不到要迭代的对象，于是产生错误。就是说迭代器在工作的时候，是不允许被迭代的对象被改变的。 

"""