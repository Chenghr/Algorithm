size = int(input())
line = input().strip()
nums = list(map(int, line.split()))
nums_sort = nums[:]
nums_sort.sort()

ans = len(nums_sort)
for i in range(len(nums_sort)):
    if i != nums_sort[i]:
        ans = i
        break

for num in nums:
    print(min(ans, num))