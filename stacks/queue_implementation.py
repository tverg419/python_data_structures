class Queue:

    def __init__(self):
        self.queue = []
    
    # adds a new item to the back of the queue
    def enqueue(self, value):
        self.queue.insert(0, value)
    
    # removes from the front of the queue
    def dequeue(self):
        return self.queue.pop()
    
    # returns if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[len(self.queue) - 1]
    # returns the size of the queue
    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.peek())
    print('Working')