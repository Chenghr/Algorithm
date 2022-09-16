"""
    题目描述:
        给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。
        你可以按 任意顺序 返回答案。

    提示:
        1 <= nums.length <= 105
        k 的取值范围是 [1, 数组中不相同的元素的个数]
        题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

    进阶: 你所设计算法的时间复杂度必须优于 O(n log n) ，其中 n 是数组大小。

    链接: https://leetcode-cn.com/problems/top-k-frequent-elements
"""

"""
    思路:
        1. 暴力思想: O(nlogn) + O(n)
            a. 遍历数组，获得统计每个元素出现的频次;（map的思想）
            b. 遍历 map，获得元素与频次对应的元组，加入 list 中，注意频次在前，然后对 list 排序;
            c. 将 list 前 k 个元组中的元素加入到集合中，返回即可。

            python 中 sort 方法的介绍: 
            https://www.runoob.com/python/att-list-sort.html
        
        2. 堆: O(nlogk) + O(n)
            与 1 中的思想类似，不同的是，维护一个总长为 k 的小顶堆，避免完整排序，排序复杂度降低。
            用小顶堆，因为要统计最大前k个元素，只有小顶堆每次将最小的元素弹出，最后小顶堆里积累的才是前k个最大元素。

            python实现堆的方法介绍:
            https://blog.csdn.net/qq_23869697/article/details/82735088
            https://docs.python.org/zh-cn/3/library/heapq.html
        
        3. 快速排序改版(绝杀): 平均O(n) + O(n)
            使用基于快速排序的方法，求出「出现次数数组」的前 k 大的值。
            
            - 快排步骤
                a. 随机选一个中间值作为基准，将它与最左侧元素交换;
                b. 从第 2 个元素开始遍历，遍历过程中，要把比基准大的挪到左边，比基准小的挪到右边;
                c. i 指向比基准大的元素，只要 j 指向的元素比基准大，就把 j 位置的元素和 i 后面一个位置的元素对调
                   并且 i 后移一位，这样 i 指向的元素以及 i 之前的元素都是比基准大的元素(基准本身除外);
                d. j 遍历到末尾后，此时 i 指向的就是排序后的列表中比基准大的最后一个元素，将该元素和基准对调;

                排序后的列表就是在 i 位置前的都比基准大，i 位置后的都比基准小

            - 分治
                a. 如果 i == k - 1，也就是i及之前的元素恰好组成了我们想要的topK，直接返回前k个元素
                b. 如果 i > k - 1, 也就是 i 及之前的元素组成了top(K+N)，要对前 i 个元素再进行一次快排，从top(K+N)里选出topK
                   findTopK(num_cnt, k, low, i - 1)
                c. 如果 i < k - 1，也就是 i 及之前的元素组成了top(K-N)，要对i之后的元素再进行快排，在之后的元素中选出topN
                   findTopK(num_cnt, k, i + 1, high)
                返回快排结果中的数字部分
"""
from collections import defaultdict
import heapq
import random

class Solution:
    def topKFrequent_naive(self, nums: list[int], k: int) -> list[int]:

        # 统计频率信息
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        
        freq_num = []
        for key, freq in dic.items():
            freq_num.append((freq, key))

        # 降序排序
        freq_num.sort(reverse=True)
        
        # 获取结果
        result = []
        for i in range(k):
            result.append(freq_num[i][1])
        
        return result

    def topKFrequent_heap(self, nums: list[int], k: int) -> list[int]:

        # 统计频率
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        # 对频率排序，维护一个大小为 k 的小顶堆
        minHeap = []
        for key, freq in dic.items():
            heapq.heappush(minHeap, (freq, key))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # 获取结果，由于是小顶堆，所以逆序输出
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(minHeap)[1]
        
        return result

    def topKFrequent_quickSort(self, nums: list[int], k: int) -> list[int]:

        # 统计频率信息
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        
        freq_num = []
        for key, freq in dic.items():
            freq_num.append((freq, key))
        
        # 获取 topk 对应的元组
        topKs = self._findTopK(freq_num, k, 0, len(freq_num)-1)

        # 获得结果
        result = [item[1] for item in topKs]  # 对顺序不敏感

        return result
    
    def _findTopK(self, freq_num, k, low, high):
        """
        - 快排步骤
                a. 随机选一个中间值作为基准，将它与最左侧元素交换;
                b. 从第 2 个元素开始遍历，遍历过程中，要把比基准大的挪到左边，比基准小的挪到右边;
                c. i 指向比基准大的元素，只要 j 指向的元素比基准大，就把 j 位置的元素和 i 后面一个位置的元素对调
                   并且 i 后移一位，这样 i 指向的元素以及 i 之前的元素都是比基准大的元素(基准本身除外);
                d. j 遍历到末尾后，此时 i 指向的就是排序后的列表中比基准大的最后一个元素，将该元素和基准对调;

                排序后的列表就是在 i 位置前的都比基准大，i 位置后的都比基准小
        """
        # 选择基准点
        pivot = random.randint(low, high)
        freq_num[low], freq_num[pivot] = freq_num[pivot], freq_num[low]

        i = low
        for j in range(low+1, high+1):
            if freq_num[j][0] > freq_num[low][0]:
                freq_num[i+1], freq_num[j] = freq_num[j], freq_num[i+1]
                i += 1
                # 这里 j 不用做位置变化，j 大于 i，等于已经确认 i+1 位置的元素小于基准
        
        freq_num[low], freq_num[i] = freq_num[i], freq_num[low]\
        
        # 分治
        if i == k-1:
            return freq_num[ : k]
        elif i > k-1:
            return self._findTopK(freq_num, k, low, i-1)
        else:
            return self._findTopK(freq_num, k, i+1, high)

    def _findTopK_wrong(self, freq_num, k, low, high):
        """基于快排的思想实现，降序排列
        错误的实现方法，结果不稳定，有问题。。。
        """
        # 选择基准点
        pivot = random.randint(low, high)
        freq_num[low], freq_num[pivot] = freq_num[pivot], freq_num[low]

        # 一趟快排
        left, right = low+1, high
        while left < right:

            while freq_num[right][0] <= freq_num[low][0] and left < right:
                right -= 1

            while freq_num[left][0] >= freq_num[low][0] and left < right:
                left += 1
            
            freq_num[left], freq_num[right] = freq_num[right], freq_num[left]
            
        # 使划分好的数分布在基数两侧
        # 注意此处由于 left 增加了1，所以仅能保证 left-1 是大于基准值，因此与 left-1 交换
        freq_num[low], freq_num[left-1] = freq_num[left-1], freq_num[low]

        # 分治
        if left == k:
            return freq_num[ : k]
        elif left > k-1:
            return self._findTopK(freq_num, k, low, left-2)
        else:
            return self._findTopK(freq_num, k, left, high)

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    # nums = [1]
    # k = 1
    
    # result = solution.topKFrequent_naive(nums, k)
    # result = solution.topKFrequent_heap(nums, k)
    result = solution.topKFrequent_quickSort(nums, k)
    print(result)