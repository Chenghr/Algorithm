from queue import PriorityQueue

def calMinSteps(num1, num2):
    visited = set()
    que = PriorityQueue()
    que.put((0, num1, num2))

    while que.qsize() != 0:
        steps, num1, num2 = que.get()

        if num1 == num2:
            return steps

        visited.add((num1, num2))
        
        if (num1*2, num2) not in visited:
            que.put((steps+1, num1*2, num2))
        if (int(num1/2), num2) not in visited:
            que.put((steps+1, int(num1/2), num2))
        if (num1+1, num2) not in visited:
            que.put((steps+1, num1+1, num2))

        if (num1, num2*2) not in visited:
            que.put((steps+1, num1, num2*2))
        if (num1, int(num2/2)) not in visited:
            que.put((steps+1, num1, int(num2/2)))
        if (num1, num2+1) not in visited:
            que.put((steps+1, num1, num2+1))

    return -1

def getPath(num, target):
    visited = set()
    que = PriorityQueue()
    path = dict()
    que.put((0, num))

    while que.qsize() != 0:
        steps, num = que.get()
        path[num] = steps

        if num == target:
            break
        
        visited.add(num)
        
        if num + 1 not in visited:
            que.put((steps+1, num+1))
        
        if num * 2 not in visited:
            que.put((steps+1, num*2))
        
        if int(num/2) not in visited:
            que.put((steps+1, int(num/2)))
    
    return path

def calMinSteps_v1(num1, num2):
    path1 = getPath(num1, num2)
    path2 = getPath(num2, num1)

    minSteps = min(path1[num2], path2[num1])
    for key in path1.keys():
        if key in path2:
            minSteps = min(minSteps, path1[key]+path2[key])

    return minSteps
    
if __name__ == "__main__":
    a, b = map(int, input("").split())
    
    minSteps = calMinSteps(a, b)
    print(minSteps)