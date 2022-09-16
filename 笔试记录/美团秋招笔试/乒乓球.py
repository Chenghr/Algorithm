line = input().strip()
nums = list(map(int, line.split()))

if nums[1] <= 9:
    ans = max(11 - nums[0], 0)
else:
    ans = max(nums[1]+2 - nums[0], 0)

print(ans)