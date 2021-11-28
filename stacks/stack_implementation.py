class Stack:

    # initializes a Stack 
    def __init__(self):
        self.stack = []
    
    # adds a new item to the top of the stack
    def push(self, value):
        self.stack.append(value)
        print(f'{value} was added to the stack')
    
    # removes and returns the last item in a stack
    def pop(self):
        return self.stack.pop()

    # returns the top of the stack 
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # returns if the stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # returns the length of the stack
    def size(self):
        return len(self.stack)

    # takes a list as an input and adds it to the stack
    def generate(self, nums):

        for num in nums:
            self.push(num)

if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    s.generate([1, 2, 3])
    print(s.peek())
    
    print(s.isEmpty())
    s.pop()
    s.pop()    
    s.pop()    
    print(s.isEmpty())
    s.push(4)
    print("Working")