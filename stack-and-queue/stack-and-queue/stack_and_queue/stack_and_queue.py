
class Node:
    """
    This class is used to instantiate nodes and a pointer to refer to it's next Node called next
    """

    def __init__(self, value):
        self.value  = value
        self.next = None


class Stack:
    """
    This is the stack class, it's used to create a stack of a top on None 
    """
    def __init__(self,node=None):
        self.top=node
        
    def is_empty(self):
            """
            This method is used to check is a sack contains elements 
            """
            if self.top== None:
                return True
            return False 
 

    def __str__(self):
        """
        This method os to return the stack printed 
        """
        printed_stack = ""
        
        if self.top is None:
            printed_stack = ('Add Nodes to the stack!')
        else: 
            current = self.top
            while current:
                printed_stack += f'\n  {current.value}  \n'
                current = current.next
        return printed_stack
    
    def push(self, value):
        """This element is used to add the value argument as an element in the stack """

        new_node = Node(value)
        new_node.next, self.top = self.top, new_node

    def pop(self):
        """This method removes the node from the top of the stack, and returns the node’s value."""

        if not self.is_empty():
            temp, self.top = self.top, self.top.next
            temp.next = None
            return temp.value
        else:
            return None

    def peek(self):
        """This method that returns the value of the node which is the top of the stack, without removing it from the stack."""

        if not self.is_empty():
            return self.top.value
        else:
            return None



class Queue:
    """class Queue which implements Queue data structure with its common methods"""

    def __init__(self):
        """Initiate class"""

        self.front = None
        self.rear = None

    def is_empty(self):
        """method to check if Queue is empty"""

        if self.front == None:
            return True
        return False


    def enqueue(self, value):
        """Method that takes any value as an argument and adds a new node with that value to the back of the queue """

        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Method that removes the node from the front of the queue, and returns the node’s value."""

        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            return None

    def peek(self):
        """Method that returns the value of the node located in the front of the queue, without removing it from the queue."""

        if not self.is_empty():
            return self.front.value
        return None



# if __name__=='__main__':
#     st= Stack()
#     st.push(1)
#     st.push(2)
#     st.push(3)

#     st.__str__()