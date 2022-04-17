class Node:
    """
    Class Node to create Node instances that we will build stacks and queues out of them
    """
    def __init__(self, vlaue):
        self.value=vlaue;
        self.next=None




class Stack:
    """
    class stack for implementing stack data structure methods 
    """
    def __init__(self):
       self.top=None

    def is_empty(self):
        """
        Method to check if a stack has no nodes in it 
        """
        if self.top==None:
            return True
        return False


    def push(self, value):
        """
        Method takes any value as an argument and adds a new node with that value to the top of the stack
         """

        new_node = Node(value)
        new_node.next, self.top = self.top, new_node

    def pop(self):
        """
        Method that removes the node from the top of the stack, and returns the node’s value.
        """

        if not self.is_empty():
            temp, self.top = self.top, self.top.next
            temp.next = None
            return temp.value
        else:
            return None

    def peek(self):
        """
        Method that returns the value of the node located on top of the stack,
         without removing it from the stack.
        """

        if not self.is_empty():
            return self.top.value
        else:
            return None


class PseudoQueue:
    def __init__(self, stk1):
        """
        Initiate PseudoQueue class with one empty and one given stack
        """
        self.stk1 = stk1
        self.stk2 = Stack()

    def enqueue(self, value):
        """
        Method to inserts value into the PseudoQueue, using a first-in, first-out approach.
        """
        self.stk1.push(value)

    def dequeue(self):
        """"
        Method to extract a value from the PseudoQueue, using a first-in, first-out approach. 
        Returns value of extracted node 
        it uses two stacks to do this 
        """

        if self.stk1.top == None:
            raise Exception("PseudoQueue is empty")
        while self.stk1.top != None:
            poped_node = self.stk1.pop()

            self.stk2.push(poped_node)

        poped_value = self.stk2.pop()

        while self.stk2.top != None:
            self.stk1.push(self.stk2.pop())
        return poped_value
