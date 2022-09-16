
# If you need to import additional packages or classes, please import here.
from queue import PriorityQueue

def func():
    n = int(input(""))
    target = int(input(""))

    indegree = []  # 每个节点的入度
    graph = [[0] * n for _ in range(n)]
    que = PriorityQueue()  # 入度为 0 的节点

    for end in range(n):
        # 输入 n 个服务的依赖
        nums = list(map(int, input("").split(',')))
        indegree.append(nums[0])

        if nums[0] == 0:
            que.put(end)

        begins = nums[1: ]
        for begin in begins:

            if begin <= -1 or begin >= n:
                print(None)
                return
                
            graph[begin][end] = 1
    
    outPut = []
    while que.qsize() != 0:
        begin = que.get()
       
        if begin == target:
            for i in range(len(outPut)-1):
                print(outPut[i], end=',')
            print(outPut[-1])
            
            return 
        
        outPut.append(begin)

        for end in range(n):
            # 删除 begin 节点
            if graph[begin][end] == 1:
                indegree[end] -= 1

                if indegree[end] == 0:
                    que.put(end)
    
    print(-1)
    return 
        

if __name__ == "__main__":
    func()
