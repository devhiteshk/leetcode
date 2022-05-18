class MyQueue:

    def __init__(self):
        self.Queue = []

    def push(self, x: int) -> None:
        self.Queue.append(x)

    def pop(self) -> int:
        return self.Queue.pop(0)

    def peek(self) -> int:
        return self.Queue[0]

    def empty(self) -> bool:
        if self.Queue == []:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()