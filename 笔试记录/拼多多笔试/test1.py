from collections import defaultdict

while True:
    try:
        n = int(input(""))
        nums = list(map(int, input("").split()))

        dic = defaultdict(list) # 颜色，上一次出现的下标，gap，是否第一次出现，是否满足条件

        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = [i, -1, True]
            else:   
                if not dic[num][-1]:
                    # 不满足等差
                    continue

                if dic[num][1] == -1:
                    # 更新gap
                    dic[num][1] = i - dic[num][0]
                else:
                    if i - dic[num][0] == dic[num][1]:
                        dic[num][0] = i
                    else:
                        dic[num][-1] = False
        
        ans = []
        
        for item in dic.items():
            if item[1][-1] == True:
                if item[1][1] == -1:
                    ans.append((item[0], 0))
                else:
                    ans.append((item[0], item[1][1]))
                
        ans.sort()
        
        print(len(ans))
        for num, gap in ans:
            print(num, gap)
            
    except:
        break
