 # Linked List 

# Create a Node class to create a node
class Node:
    def __init__(self, data, next=None): #next will be None until not provided by the user
        self.data = data
        self.next = None # Initially when a node is created it does not point to any other node

# Create a LinkedList class
class LinkedList:  # Class to form a linked list
    def __init__(self):
        self.head = None # If head is None, it means the linked list is empty.

    # Method to add a node at the beginning of the LL
    def insertAtBegin(self, data):
        new_node = Node(data) # data being stored in the node created 
        new_node.next = self.head # value of head is current node because this is the first node
        self.head = new_node # value of head is changed to the next node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if index == 0:  #  the new node should be inserted at the beginning.
            self.insertAtBegin(data)
            return

        position = 0  # keeps track of the current index during traversal.
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    # Update node at a given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            current_node.data = val
        else:
            print("Index not present")

    # Method to remove first node of linked list
    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):
        if self.head is None:
            return

        # If there's only one node
        if self.head.next is None:
            self.head = None
            return

        # Traverse to the second last node
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    # Method to remove a node at a given index
    def remove_at_index(self, index):
        if self.head is None:
            return

        if index == 0:
            self.remove_first_node()
            return

        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    # Method to remove a node from the linked list by its data
    def remove_node(self, data):
        current_node = self.head

        # If the node to be removed is the head node
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return

        # Traverse and find the node with the matching data
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # If the data was not found
        print("Node with the given data not found")

    # Print the size of the linked list
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    # Print the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


How to use this linked list 

node1 = Node(10)                # First node (next defaults to None)
node2 = Node(20, node1)    

The above is how we will call the class and create an object(node) . Other class is for linked list, 

# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Node Data:")
llist.printLL()

# remove nodes from the linked list
print("\nRemove First Node:")
llist.remove_first_node()
llist.printLL()

print("\nRemove Last Node:")
llist.remove_last_node()
llist.printLL()

print("\nRemove Node at Index 1:")
llist.remove_at_index(1)
llist.printLL()

# print the linked list after all removals
print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value at Index 0:")
llist.updateNode('z', 0)
llist.printLL()

print("\nSize of linked list:", llist.sizeOfLL())


- capacity for the list allocated 
- when inserting it will put the values 
- inserting in between to create space many operations 
- dynamic array allocates *2 memory locations 
- don't have to copy values unlike array in linked list 
- so no need to pre-allocate space and insertion is easier


In Python, variables do not hold actual objects; they hold references (memory addresses) to those objects.

The newest node always becomes the head (the first node).

The older nodes get pushed further down the list.

This means the first node you insert will be at the end of the list.

class LinkedList:  # Class to form a linked list
    def __init__(self):
        self.head = None # If head is None, it means the linked list is empty.

    # Method to add a node at the beginning of the LL
    def insertAtBegin(self, data):
        new_node = Node(data) # data being stored in the node created 
        new_node.next = self.head # value of head is current node because this is the first node
        self.head = new_node

Now look, 

[30] → [20] → [10] → None 

This is how it will happen, so the first node has head 10 and no next, in the following iteration 20 will now be the head, 10 will be pushed and 10 will become the next for
the new node -> self.head → [20 | next] → [10 | None] # something like this 

So basically next is pointing towards the node with head 10. 

C – Uses pointers explicitly for memory references.

C++ – Supports both references (easier to use) and pointers (more manual control).

Python – Objects are referenced, primitives (like int, float) are passed by value.

Java – Objects (instances of classes) are referenced; primitive types (e.g., int, float, boolean) are by value.

