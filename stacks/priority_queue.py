'''
We want the priority queue to be sorted so that the operations are less expensive
Utilize a doubly linked-list because insertion is less expensive compared to using an array

'''
    
class PriorityQueue:

    # creates a dictionary that holds ids and priorities
    def __init__(self):
        self.items = {}

    # inserts the new element into a sorted array
    def insert(self, id, val):
        if val not in self.items.values():
            self.items[id] = val
        else:
            print(f"Priority {val} already exists in queue")
    
    # removes the element given an id
    def remove(self, id):
        if id in self.items.keys():
            del self.items[id]
        else:
            print(f"Could not find element with id: {id}")
    
    # updates a given element
    def update_element(self, id, val):
        
        if id in self.items.keys():
            
            if val not in self.items.values():
                self.items[id] = val
            else:
                print(f"Priority {val} already exists in queue")
        else:
            self.insert(id, val)
    
    # extracts from the beginning of the queue
    def extract_max(self):
        keys = list(self.items.keys())
        id = keys[len(self.items) - 1]
        return self.items.pop(id)

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert("Get a Job", 1)
    pq.insert("make some money", 2)
    print(pq.extract_max())
    print(pq.items)