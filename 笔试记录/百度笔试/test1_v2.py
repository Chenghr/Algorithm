

if __name__ == '__main__':
    n = int(input(""))
    nums = list(map(int, input("").split()))

    nums.sort()
    maxNum, maxCount = -float('inf'), 0
    minNum, minCount = float('inf'), n+1
    
    i = 0
    while i < len(nums):

        j = i + 1

        while j < len(nums) and nums[j] == nums[i]:
            j += 1
        
        if maxCount < j - i:
            maxNum = nums[i]
            maxCount = j - i
        elif maxCount == j - i:
            maxNum = nums[i]  # 排序了，后来的大
        
        if minCount > j - i:
            # 排序了，先来的小
            minNum = nums[i]
            minCount = j - i
        
        i = j
    
    print(maxNum - minNum)