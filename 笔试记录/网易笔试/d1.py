import sys 

if __name__ == "__main__":

    line = sys.stdin.readline().strip()
    x1, y1, x2, y2, x3, y3 = map(int, line.split())
    
    line = sys.stdin.readline().strip()
    v1, d1 = map(int, line.split())

    line = sys.stdin.readline().strip()
    v2, d2 = map(int, line.split())

    l_ab = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    l_ac = ((x3-x1)**2 + (y3-y1)**2) ** 0.5
    l_bc = ((x3-x2)**2 + (y3-y2)**2) ** 0.5

    ans = 0 
    if v1 == v2:
        ans = -1
    elif d1 == 0:
        if d2 == 0:
            if v1 < v2:
                ans = (l_bc + l_ac) / (v2 - v1)
            else:
                ans =  l_ab / (v1 - v2)
        else:
            ans = l_ab / (v1 + v2)
    elif d1 == 1:
        if d2 == 0:
            ans = (l_ac + l_bc) / (v1 + v2)
        elif d2 == 1:
            if v1 < v2:
                ans = l_ab / (v2 - v1)
            else:
                ans = (l_bc + l_ac) / (v1 - v2)
    
    print(ans)