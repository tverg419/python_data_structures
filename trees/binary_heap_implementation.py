class BinaryHeap:

    # note: the heap is initialized with position 0 so that all index can utilize integer division
    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    # uses the sift_up method as a helper when adding a new node
    def insert(self, node):
        self.heap.append(node)
        self.size += 1
        self.sift_up(self.size)

    # this method checks if the node at a given index is in the correct position
    def sift_up(self, index):
        while index // 2 > 0:
            if self.heap[index] < self.heap[index // 2]:
                temp = self.heap[index // 2]
                self.heap[index // 2] = self.heap[index]
                self.heap[index] = temp
            index = index // 2
    # uses the get min child func as a helper funciton to retrieve the index of the min child
    # this method checks if the node at the given index is in the correct position and will sift it down to the smalledt child
    def sift_down(self, index):
        while 2*index <= self.size:
            min_index = self.get_min_child(index)
            if self.heap[index] > self.heap[min_index]:
                temp = self.heap[index]
                self.heap[index] = self.heap[min_index]
                self.heap[min_index] = temp
            index = min_index

    def get_min_child(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heap[index*2] < self.heap[index*2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def get_min(self):
        return self.heap[1]
    
    def delete_min(self):
        min_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sift_down(1)
        return min_value

    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def build_heap(self, l):
        index = len(l) // 2
        self.size = len(l)
        self.heap = [0] + l[:]
        while(index > 0):
            self.sift_down(index)
            index = index -1
    
    def get_heap(self):
        return self.heap
        
bh = BinaryHeap()
numbers = [3, 11, 10, 4, 5, 6, 7, 3]
bh.build_heap(numbers)
print(bh.get_heap())
print(bh.delete_min())
print(bh.get_min())
print(bh.delete_min())
print(bh.get_min())
