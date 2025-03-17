# Binary Tree

Binary tree is a tree data structure in which each node has at most two children. 

    # Constructed binary tree is
    #         1   Root Node
    #        / \
    #       2   3  Child Nodes
    #      / \
    #     4   5 Leaf Nodes cuz no children, also 4-5 are sibling nodes 


Let's say we have to make this binary tree. In this first is to make a Node class

class Node:
    def __init__(self, x):   # this constructor is initializing a node in the class
        self.data = x
        self.left = None
        self.right = None
# Below are the values by calling the node class and storing them in variable root which is indirectly calling the getSize function
root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4) 
    root.left.right = Node(5) 
  
# Python program to find the size
# of a binary tree.

class Node:
    def __init__(self, x):   # This constructor is initializing a node in the class
        self.data = x
        self.left = None
        self.right = None 

# Recursive function to find the 
# size of binary tree.
def getSize(root):
    if root is None:
        return 0

    # Find the size of left and right 
    # subtree.
    left = getSize(root.left) # This is recusrsion because the function getSize is getting called within the function
    right = getSize(root.right)

    # return the size of curr subtree.
    return left + right + 1

if __name__ == "__main__":

    # Constructed binary tree is
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(getSize(root))
