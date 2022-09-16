if __name__ == "__main__":
    n, m = map(int, input("").split())
    left = list(map(int, input("").split()))  # 1-based
    right = list(map(int, input("").split()))

    prefix = [0] * (n+1)  # 差分数组

    for i in range(m):
        prefix[left[i]] += 1

        if right[i] + 1 <= n:
            prefix[right[i]+1] -= 1
    
    count = 0
    for i in range(1, n+1):
        prefix[i] += prefix[i-1]

        if prefix[i] > 1:
            count += 1
    
    print(count)