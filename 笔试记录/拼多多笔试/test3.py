while True:
    try:
        n, m = map(int, input("").split())

        # 下标从1 开始
        candidates = [True] * (m+1)

        nums = list(map(int, input("").split()))
        
        for num in nums:
            candidates[num] = False

        q = int(input(""))

        for _ in range(q):
            l, r = map(int, input("").split())

            ans = -1
            for i in range(l, r+1):
                if candidates[i]:
                    ans = i
                    break
            
            print(ans)
    except:
        break

n, m = int(input("").split())

# 下标从1 开始
candidates = [True] * (m+1)

nums = list(map(int, input("").split()))

for num in nums:
    candidates[num] = False

q = int(input(""))

for _ in range(q):
    l, r = int(input("").split())

    ans = -1
    for i in range(l, r+1):
        if candidates[i]:
            ans = i
            break
    
    print(ans)

