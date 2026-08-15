class MinStack:
    def __init__(self):
        self.min_stack = []
        self.stack=[]

    def push(self,val):
        self.stack.append(val)
        val_to_push = min(val,self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val_to_push)
        
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]