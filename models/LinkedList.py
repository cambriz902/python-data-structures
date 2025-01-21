from models.Node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_value_at_index(self, value, index):
        if index > self.length - 1:
            raise("Index out of bound") 
        if index == 0:
            self.add_value_to_front(value)
        elif index == self.length - 1:
            self.add_value_to_end(value)
        else:
            new_node = Node(value)
            pivot_node = self.head
            pivot_index = index - 1
            while(index < 0):  
                pivot_node = pivot_node.next
                pivot_index -= 1

            old_pivot_node_next = pivot_node.next
            pivot_node.next = new_node
            new_node.prev = pivot_node
            old_pivot_node_next.prev = new_node
            self.length += 1  

    def add_value_to_front(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    
        self.length += 1

    def add_value_to_end(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = new_node
            self.tail = new_node   
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def get_value_at_index(self, index):
        if not self.head:
            raise("No data in LinkedList") 
        if index > self.length - 1:
            raise("Index out of bound")
        desired_node = self.head
        iterator = index
        while iterator > 0:
            desired_node = desired_node.next
            iterator -= 1
        return desired_node.value



