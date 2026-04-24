class MinStack:

    def __init__(self):
        self.stack = []
        self.minSt = []

    def push(self, val: int) -> None:
        if not self.minSt or  val <= self.minSt[-1]:
            self.minSt.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minSt[-1]:
            self.minSt.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minSt[-1]
        
