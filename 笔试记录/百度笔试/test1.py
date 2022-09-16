from collections import defaultdict

if __name__ == '__main__':
    n = int(input(""))
    nums = list(map(int, input("").split()))

    dic = defaultdict(int)
    maxNum, maxCount = -float('inf'), 0
    minNum, minCount = float('inf'), n+1
    
    for num in nums:
        dic[num] += 1

        if maxCount < dic[num]:
            maxNum = num
            maxCount = dic[num]
        elif maxCount == dic[num]:
            maxNum = max(maxNum, num)
        
        if minCount > dic[num]:
            minNum = num
            minCount = dic[num]
        elif minCount == dic[num]:
            # 这里逻辑有问题，不能保证 num 后续不再出现
            minNum = min(minNum, num)
    
    print(maxNum - minNum)