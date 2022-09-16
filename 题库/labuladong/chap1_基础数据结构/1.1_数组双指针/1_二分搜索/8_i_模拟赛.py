"""
    题目描述:

        有三种难度的题目难度分别为Easy,Medium,Hard。现在你总共有 E+EM+M+MH+H 道题，各个字符串的含义如下:
            E表示有E道题目难度为Easy。
            EM表示有EM道题目难度可以为Easy或Medium。
            M表示有M道题目难度为Medium。
            MH表示有MH道题目难度可以为Medium或Hard。
            H表示有H道题目难度为Hard。

        你要用这些题目出尽量多的模拟赛，为了保证题目质量且含有一定的区分度，每场模拟赛需要包含Easy,Medium,Hard 三种难度的题目各一道。
        求你最多能出多少场模拟赛。

    输入描述: 一行五个整数E,EM,M,MH,H; 0 <= E+EM+M+MH+H <= 1018

    链接: https://www.nowcoder.com/questionTerminal/16ea0c94aaa1497cbbe913ee0dab9159?f=discussion
"""

def find(i, E, EM, M, MH, H):
    # 容易题不够，从EM中搬
    if E < i:
        # 容易题的剩余数量比场数小
        cur = min(i - E, EM)
        E += cur
        EM -= cur
    # 难题不够，从MH中搬
    if H < i:
        # 难题的剩余数量比场数小
        cur = min(i - H, MH)
        H += cur
        MH -= cur
    # 模拟赛数量还可以往多了办(由于EM和MH分别被搬到E和H了，所以算作中等题)
    if M + EM + MH >= i and E >= i and H >= i:
        # 如果容易题、中等题、难题都够了，那就还可以办更多的比赛
        return True
    return False
 
if __name__ == "__main__":
    [E, EM, M, MH, H] = list(map(int, input().split()))
    max_val = (E + EM + M + MH + H) // 3     # 每场模拟赛三道题，此时为模拟赛场数的上限
    res = 0
    left, right = 0, max_val
    # 通过二分法来判断能否满足出题要求
    while left <= right:
        mid = (left + right) // 2
        if find(mid, E, EM, M, MH, H):
            left = mid + 1
            res = max(res, mid)
        else:
            # 场数太多，收缩右边界
            right = mid - 1
    print(res)