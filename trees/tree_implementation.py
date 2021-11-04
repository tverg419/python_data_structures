class BinaryTree(object):
    
    # constructor for BinaryTree Node that takes in a key, left and right
    def __init__(self, root, left=None, right=None):

        self.value = root
        self.left  = left
        self.right = right
    # method used to insert node to left child
    def insert_left(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t
    # method used to insert node to right child    
    def insert_right(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t
    
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def set_root(self, node):
        self.value = node
    
    def get_root(self):
        return self.value
    
def preorder_traversal(tree):
    if tree:
        print(tree.get_root())
        preorder_traversal(tree.get_left_child())
        preorder_traversal(tree.get_right_child())

def inorder_traversal(tree):
    if tree:
        inorder_traversal(tree.get_left_child())
        print(tree.get_root())
        inorder_traversal(tree.get_right_child())

def postorder_traversal(tree):
    if tree:
        postorder_traversal(tree.get_left_child())
        postorder_traversal(tree.get_right_child())
        print(tree.get_root())
'''
     3
    / \
   2   4
  /     \
 1       5     
'''
bt = BinaryTree(3)
bt.insert_left(1)
bt.insert_right(5)
bt.insert_left(2)
bt.insert_right(4)
print(preorder_traversal(bt))
print(inorder_traversal(bt))
print(postorder_traversal(bt))
