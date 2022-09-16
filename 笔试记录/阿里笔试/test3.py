if __name__ == "__main__":
    n = int(input(''))
    nums = list(map(int, input('').split()))

    i = 1
    while i < len(nums) and nums[i] > nums[i-1]:
        i += 1
    
    j = i
    while 
