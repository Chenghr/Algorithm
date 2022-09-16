class CQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def appendTail(self, value: int) -> None:
        self.inStack.append(value)

    def deleteHead(self) -> int:
        if len(self.inStack) == 0 and len(self.outStack) == 0:
            return -1
        
        if len(self.outStack) == 0:
            while len(self.inStack) != 0:
                self.outStack.append(self.inStack.pop())

        head = self.outStack.pop()
        return head

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()