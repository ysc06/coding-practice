class MinStack:
    
    def __init__(self):
        self.lst = []
        self.history = []
    
    def push(self, val: int) -> None:
        if not self.history or val <= self.history[-1]:
            self.history.append(val)
        self.lst.append(val)
        return self.lst

    def pop(self) -> None:
        num = self.lst.pop()
        if num == self.history[-1]:
            self.history.pop()
        return num
      

    def top(self) -> int:
        return self.lst[-1]
        

    def getMin(self) -> int:
   
        return self.history[-1]
