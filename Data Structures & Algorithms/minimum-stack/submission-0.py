class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minVal == None:
            self.minVal = val
        else:
            self.minVal = min(self.minVal, val)        

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()

            if popped == self.minVal:
                if self.stack:
                    self.minVal = min(self.stack)
                else:
                    self.minVal = None        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None        

    def getMin(self) -> int:
        return self.minVal
        
