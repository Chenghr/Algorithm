
# If you need to import additional packages or classes, please import here.
import sys
from collections import defaultdict
from queue import PriorityQueue

class wordCount:
    def __init__(self, word, tC, aC, rT, tO, rA, aO):
        self.word = word
        self.tC = tC  # 标题中出现次数
        self.aC = aC  # 正文中出现次数

        self.rT = rT  # 第一次出现在标题中的轮次
        self.tO = tO  # 第一次出现在标题中的轮次中的次序

        self.rA = rA  # 第一次出现在正文时的轮次
        self.aO = aO  # 第一次出现在正文中的次序

def __lt__(a: wordCount, b: wordCount):
    if a.tC*3 + a.aC == b.tC*3 + b.aC:
        # 出现词的频率大小排序
        
        if a.tC == b.tC:
            # 词频相同，先比较标题中出现的次数
            if a.rT == b.rT:
                # 进一步比较标题出现的轮次
                if a.tO == b.tO:
                    # 相同轮次比较出现的顺序
                    if a.rA == b.rA:
                        return a.aO > b.aO
                    # 标题出现顺序相同则比较正文中出现的顺序
                    return a.rA > b.rA
                else:
                    # 越晚出现越靠前
                    return a.tO > b.tO
            else:
                return a.rT < b.rT
        else:
            return a.tC < b.tC
    
    
    else:
        return a.tC*3 + a.aC < b.tC*3 + b.aC
    
wordCount.__lt__ = __lt__

def func():
    # 输出词频最高的词语个数，文章数目
    topN, m = map(int, input("").split())
    
    memory = []
    dic = defaultdict(int)

    for i in range(m):
        # 输入文章
        title = input("").split()
        article = input("").split()

        # 存储每个词的词频
        for j, word in enumerate(title):
            if word not in dic:
                memory.append(wordCount(word, 1, 0, i, j, -1, -1))
                dic[word] = len(memory)-1
            else:
                # w1 = memory[dic[word]]
                if memory[dic[word]].rT == -1:
                    memory[dic[word]].rT = i
                    memory[dic[word]].tO = j
                    memory[dic[word]].tC = 1
                else:
                    memory[dic[word]].tC += 1 
        
        for j, word in enumerate(article):
            if word not in dic:
                memory.append(wordCount(word, 0, 1, -1, -1, i, j))
                dic[word] = len(memory) - 1
            else:
                if memory[dic[word]].rA == -1:
                    memory[dic[word]].rA = i
                    memory[dic[word]].aO = j
                    memory[dic[word]].aC = 1
                else:
                    memory[dic[word]].aC += 1 
                # w1 = memory[dic[word]]
                # if w1.rA == -1:
                #     w1.rA = i
                #     w1.aO = j
                #     w1.aC = 1
                # else:
                #     w1.aC += 1 
        
    memory.sort()
    
    ans = memory[-1].word
    for i in range(len(memory)-2, len(memory)-topN-1, -1):
        w1 = memory[i]
        ans += " " + w1.word

    print(ans)
    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().

if __name__ == "__main__":
    func()
