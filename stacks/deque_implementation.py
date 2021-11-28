class Deque:

    # initializes a Stack 
    def __init__(self):
        self.items = []

    # adds a new item to the front of the deque
    def push_front(self, value):
        self.items.insert(0, value)
        print(f'{value} was added to the front of the deque')
    
    # adds a new item to the back of the deque
    def push_back(self, value):
        self.items.append(value)
        print(f'{value} was added to the back of the deque')

    # removes and returns the front item
    def pop_front(self):
        return self.items.pop(0)

    # removes and returns the back item
    def pop_back(self):
        return self.items.pop()

    # returns if the deque is empty
    def isEmpty(self):
        return len(self.items) == 0

    # returns the length of the deque
    def size(self):
        return len(self.items)

    def show_deque(self):
        return self.items

if __name__ == "__main__":
    d = Deque()
    d.push_back(1)
    d.push_back(2)
    d.push_front(3)
    print(d.show_deque())

    d.pop_front()
    d.pop_back()
    print(d.show_deque())
    print("Working")