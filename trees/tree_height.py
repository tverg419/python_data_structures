# python3

import sys
import threading


def compute_height(n, parents):
    
    nodes = [0] * n

    for i in range(n):

        node = parents[i]

        if node == -1:
            return current_max
        
        if nodes[i]:
            return nodes[i]
        
        nodes[i] = 1 + compute_height(self.parents[i])
        return parents[i]

def add_child(index):
    pass

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
