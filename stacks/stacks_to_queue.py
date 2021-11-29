'''
Stack Last In First Out
Queue: First In First Out
'''
class QueueOfStacks:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # adds to the in stack
    def enqueue(self, value):
        self.stack1.append(value)
    
    # fills the out stack if it is empty.
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__ == "__main__":
    q = QueueOfStacks()

    for i in range(5):
        q.enqueue(i)
    
    for i in range(5):
        print(q.dequeue())
