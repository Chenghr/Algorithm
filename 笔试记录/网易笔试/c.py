import sys 

def isOk(x: int, y: int, k) -> bool:
    """判断x和y末尾的0的总数是否大于等于k"""
    count = 0

    while x % 10 == 0:
        x = x // 10
        count += 1

    while y % 10 == 0:
        y = y // 10
        count += 1
    
    return count >= k

def minLength(nums: list[int], color: str, k: int):
    minLength = float('inf')

    left = 0
    x, y = 1, 1
    for right in range(0, len(nums)):
        if color[right] == 'R':
            x *= nums[right]
        else:
            y *= nums[right]

        while left <= right and isOk(x, y, k):
            minLength = min(minLength, right - left + 1)
            
            if color[left] == 'R':
                x /= nums[left]
            else:
                y /= nums[left]
            
            left += 1
    
    return minLength

if __name__ == "__main__":

    line = sys.stdin.readline().strip()
    n, k = map(int, line.split())
    
    line = sys.stdin.readline().strip()
    nums = list(map(int, line.split()))

    color = sys.stdin.readline()
    
    ans = minLength(nums, color, k)
    print(ans)