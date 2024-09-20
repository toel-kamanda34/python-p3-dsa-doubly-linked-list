class Node:
    def __init__(self, data,next_node = None, prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    
class DoublyLinkedList:

    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def append(self, node):
        if self.head == Node:
            self.head = node
            self.tail = node
            return
        node.prev_node = self.tail
        self.tail.next_node = node
        self.tail = node

    def delete_tail(self):
        #check if the list has one node ,head and tail are the same
        if self.head == self.tail:
            #if there is only one node set the head and tail to none
            self.head = None
            self.tail = None
        #traverse the entire list to find the second_to_last node (prev)
        else:
            #access the second to last node(self.tail.prev_node)
            prev = self.tail.prev_node
            #update the tail and next_node pointers

            #disconnect the tail and update tail as the secod last node
            prev.next_node = None
            self.tail = prev